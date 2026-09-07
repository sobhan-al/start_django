from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from blog.models import Post, Category


def blog_view(request):

    posts = Post.objects.filter(status=1)
    categoryss = Category.objects.all()

    context = {
        'posts': posts,
        'categoryss': categoryss,
    }

    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):

    post = get_object_or_404(Post, pk=pid)

    posts = Post.objects.filter(status=1)
    categoryss = Category.objects.all()

    context = {
        'post': post,
        'posts': posts,
        'categoryss': categoryss,
    }

    return render(request, 'blog/blog-single.html', context)



def test(request):
    posts = Post.objects.all()
    categoryss = Category.objects.all()
    context = {'categoryss':categoryss,'posts':posts}
    return render(request,'test.html',context)