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
Commenting System: Users can comment on blog posts.
Likes: Users can like and unlike blog posts.
Tagging: Posts can be tagged, and users can filter posts by tags.
Search: Full-text search across blog posts.
Email Sharing: Share blog posts via email.
Responsive Design: Mobile-friendly design using Bootstrap.