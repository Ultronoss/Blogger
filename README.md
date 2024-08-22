**Project Name**: Django Blog Application

***Description***:

This Django-based blog application allows users to register, create, and manage their blog posts. Users can comment on posts, like posts, and share them via email. The application includes features like tagging, searching, and responsive design using Bootstrap.

**Setup Information**:

***1. Clone the repository***

`git clone https://github.com/Ultronoss/Blogger`

`cd blog_project`

***2. Set Up a Virtual Environment:***

`python3 -m venv venv`

`source venv/bin/activate`


***3. Install all dependencies:***

`pip install -r requirements.txt`


***4. Apply Migrations:***

`python manage.py makemigrations`

`python manage.py migrate`


***5. Create a Superuser:***

`python manage.py createsuperuser`


***6. Run the deployment:***

`python manage.py runserver`


***7.Access the Application:***

Open your browser and navigate to `http://127.0.0.1:8000/`.


**Feature Overview**


***User Authentication***: Register, login, and logout functionality.


***Blog Post Management***: Create, edit, and delete blog posts with rich text content.


***Commenting System***: Users can comment on blog posts.


***Likes***: Users can like and unlike blog posts.


***Tagging***: Posts can be tagged, and users can filter posts by tags.


***Search***: Full-text search across blog posts.


***Email Sharing***: Share blog posts via email.


***Responsive Design***: Mobile-friendly design using Bootstrap.

**User Guide**

1. ***Registering a New Account***

Visit the registration page and fill in your details to create a new account.

2. ***Logging In***

Use your username and password to log in.

3. ***Accessing Your Profile***

Once logged in, access your profile via the dropdown menu in the navigation bar.

4. ***Creating a Blog Post***

Navigate to the "New Post" page, fill in the title and content, and submit to publish your post.

5. ***Editing or Deleting a Blog Post***

On your profile page, select "Edit" or "Delete" for any post you want to modify or remove.

6. ***Commenting on a Post***

Open a blog post, scroll down to the comments section, and submit your comment.

7. ***Liking a Post***

Click the "Like" button on a post to like it. Click again to unlike.

8. ***Filtering by Tags***

Click on a tag under a post to see all posts with that tag.

9. ***Searching Posts***

Use the search bar in the navbar to find posts by keywords.

10. ***Sharing a Post via Email***

Click the "Share via Email" button on a post, fill in the recipient's email, and send.


**Developer Guide**
1. ***Project Structure***

- blog_project/: Root directory of the project.

- blog/: Main application directory.

- models.py: Contains all the models.

- views.py: Contains all the views.

- forms.py: Contains the forms used in the application.

- urls.py: URL routing for the application.

- templates/blog/: HTML templates.

- static/: Static files (CSS, JS).

2. ***Adding a New Feature***

- Model: Define a new model in models.py.

- View: Create a view in views.py to handle the logic.

- Template: Add or modify a template in templates/blog/.

- URL: Add a new URL pattern in urls.py to map the view.
