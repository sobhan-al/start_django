from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.db.models import Q
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_view(request,name=None,author_username=None):
    posts = Post.objects.filter(status=1)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if name:
        posts = posts.filter(categorys__name=name)

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.page(posts.num_pages)
            
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(Q(content__contains=request.GET.get('s')) | Q(title__contains=request.GET.get('s')) | Q(categorys__name__contains=request.GET.get('s')))
    context = {
        'posts': posts
    }

    return render(request, 'blog/blog-home.html', context)



def test(request):
    posts = Post.objects.all()
    categoryss = Category.objects.all()
    context = {'categoryss':categoryss,'posts':posts}
    return render(request,'test.html',context)