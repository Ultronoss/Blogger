from django.views.generic import ListView, DetailView
from .models import BlogPost, Comment, Tag
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import CommentForm, BlogPostForm, EmailPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'  
    context_object_name = 'posts'
    paginate_by = 5  
    ordering = ['-publish_date']

class BlogPostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(BlogPost, pk=pk)
        form = CommentForm()
        comments = post.comments.all()

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'blog/blog_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(BlogPost, pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.user = request.user
            comment.save()

            return redirect('blog-detail', pk=post.pk)

        comments = post.comments.all()

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'blog/blog_detail.html', context)

@login_required
def like_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(reverse('blog-detail', args=[str(pk)]))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save tags
            return redirect('blog-home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def share_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you reading '{post.title}'"
            message = f"Read '{post.title}' at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/share_post.html', {'post': post, 'form': form, 'sent': sent})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(author=user).order_by('-publish_date')
    return render(request, 'blog/profile.html', {'profile_user': user, 'posts': posts})

def search(request):
    query = request.GET.get('q')
    results = BlogPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = BlogPost.objects.filter(tags=tag)
    return render(request, 'blog/tag_posts.html', {'posts': posts, 'tag': tag})