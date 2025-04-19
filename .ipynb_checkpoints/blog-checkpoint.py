from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Index route - List all blogs
@app.route('/')
def index():
    conn = sqlite3.connect('blogs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM blogs')
    blogs = cursor.fetchall()
    conn.close()
    
    formatted_blogs = [{'id': blog[0], 'title': blog[1], 'content': blog[2].replace('\n', '<br>')} for blog in blogs]
    return render_template('index.html', blogs=formatted_blogs, role=session.get('role'))

# Add a new blog (only admin)
@app.route('/add', methods=['GET', 'POST'])
def add_blog():
    if 'username' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO blogs (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_blog.html')

# Edit an existing blog (only admin)
@app.route('/edit/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    if 'username' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        conn = sqlite3.connect('blogs.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE blogs SET title=?, content=? WHERE id=?', (title, content, blog_id))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    conn = sqlite3.connect('blogs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, content FROM blogs WHERE id=?', (blog_id,))
    blog = cursor.fetchone()
    conn.close()

    if not blog:
        return 'Blog not found', 404

    return render_template('edit_blog.html', blog=blog)

# Delete an existing blog (only admin)
@app.route('/delete/<int:blog_id>')
def delete_blog(blog_id):
    if 'username' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))

    conn = sqlite3.connect('blogs.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM blogs WHERE id=?', (blog_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin123':
            session['username'] = username
            session['role'] = 'admin'
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Incorrect username or password')
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
