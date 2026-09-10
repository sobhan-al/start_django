from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from blog.models import Post
from .models import Contact,Newsletter
from website.forms import ContactForm,NewsletterForm
from django.contrib import messages

def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'website/index.html',context)


def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited')
        else:
            messages.add_message(request,messages.ERROR,'your ticket denied')
    form = ContactForm()

    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()            
            messages.add_message(request,messages.SUCCESS,'email receive!')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,'email did not received!')
            return HttpResponseRedirect('/')
    form = NewsletterForm()

    return render(request,'base.html',{'form':form})

def elements_view(request):
    return render(request,'website/elements.html')