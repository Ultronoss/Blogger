from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, like_post, register, create_blog_post, share_post, profile,search,tag_posts
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/like/', like_post, name='like-post'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('post/new/', create_blog_post, name='create-post'),
    path('post/<int:pk>/share/', share_post, name='share-post'),
    path('profile/<str:username>/', profile, name='profile'),
    path('search/', search, name='search'),
    path('tag/<str:tag_name>/', tag_posts, name='tag-posts'),
]
