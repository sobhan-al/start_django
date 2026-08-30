from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from blog.models import Post, Category


def blog_view(request):

    posts = Post.objects.all()
    categoryss = Category.objects.all()

    for category in categoryss:
        category.post_count = Post.objects.filter(
            categorys=category
        ).count()

    context = {
        'posts': posts,
        'categoryss': categoryss,
    }

    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):

    post = get_object_or_404(Post, pk=pid)

    posts = Post.objects.all()
    categoryss = Category.objects.all()

    for category in categoryss:
        category.post_count = Post.objects.filter(
            categorys=category
        ).count()

    context = {
        'post': post,
        'posts': posts,
        'categoryss': categoryss,
    }

    return render(request, 'blog/blog-single.html', context)