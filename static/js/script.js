document.addEventListener('DOMContentLoaded', function() {
    // Attach event listeners to delete buttons
    var deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            var blogId = button.getAttribute('data-blog-id');
            var confirmDelete = confirm('Are you sure you want to delete this blog?');
            if (confirmDelete) {
                window.location.href = '/delete/' + blogId;
            }
        });
    });

    // Function to handle logout confirmation
    function confirmLogout() {
        var confirmLogout = confirm("Are you sure you want to logout?");
        if (confirmLogout) {
            window.location.href = "/logout"; // Redirect to logout route
        }
    }

    // Add event listener to the logout button
    var logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default click behavior
            confirmLogout(); // Call the confirmation function
        });
    }
});
