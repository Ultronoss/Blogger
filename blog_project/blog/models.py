from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    likes = models.ManyToManyField(User, related_name='blogpost_likes', blank=True)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog_post.title}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'