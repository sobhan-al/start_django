from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import HttpResponseRedirect,JsonResponse
from django.db.models import Q
from blog.models import Post, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from website.forms import NewsletterForm
from django.contrib import messages
from blog.forms import CommentForm

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
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.add_message(request,messages.SUCCESS,'Message sent. If your message is approved, you will be able to see it in the comments.', extra_tags="comment_input")
            return HttpResponseRedirect(request.path)
        else:
            messages.add_message(request,messages.ERROR,'message did not received!', extra_tags="comment_input")

    post = get_object_or_404(Post, pk=pid)
    comments = Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')

    context = {
        'post': post, 'comments':comments, 'form':form
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


def blog_newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.add_message(request,messages.SUCCESS,'email receive!', extra_tags="blog_ema_input")
            return HttpResponseRedirect('/')

        else:
            messages.add_message(request,messages.ERROR,'email did not received!', extra_tags="blog_ema_input")
            return HttpResponseRedirect('/')


    return render(request,'blog/blog-newsletter.html',{'form':form})

def test(request):
    posts = Post.objects.all()
    categoryss = Category.objects.all()
    context = {'categoryss':categoryss,'posts':posts}
    return render(request,'test.html',context)