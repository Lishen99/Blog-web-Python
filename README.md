# 📝 Blog Web Application (Python + Flask)

This is a lightweight blog platform built using **Python Flask** that allows users to create, edit, and view blog posts. The project includes a basic authentication system and uses SQLite for backend storage. It's ideal for learning purposes or as a starter for more complex blog platforms.

## 🚀 Features

- 🏠 Home page with all blogs listed
- 🔐 Login system for authentication
- ➕ Add a new blog post
- ✏️ Edit existing blog posts
- 🎨 Styled using custom CSS
- 📂 Organized with HTML templates and static files

## 🧠 Technologies Used

- **Backend:** Python 3, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Templating Engine:** Jinja2

## 📁 Project Structure

```
Blog-web-Python-main/
│
├── blog.py                  # Main Flask application
├── blogs.db                 # SQLite database file
│
├── static/                 # Static assets (CSS, JS)
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
│
├── templates/              # HTML templates (Jinja2)
│   ├── index.html
│   ├── add_blog.html
│   ├── edit_blog.html
│   └── login.html
│
└── README.md               # Project README
```

## 🧪 Running the App

1. **Install Flask** (if not already installed):

   \`\`\`bash
   pip install flask
   \`\`\`

2. **Run the app**:

   \`\`\`bash
   python blog.py
   \`\`\`

3. Open a browser and go to \`http://localhost:5000\`

> ⚠️ Make sure \`blogs.db\` is in the same folder as \`blog.py\`. If it doesn't exist, the app will create it automatically with the required table.

## 🔐 Default Credentials (for demo)

You may want to set default user credentials for login within \`blog.py\` for testing, or integrate a registration page.

## 🛠️ To-Do / Improvements

- Add registration functionality
- Implement better password storage (e.g., hashing)
- Add user-specific posts
- Implement pagination
- Add comment section

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
