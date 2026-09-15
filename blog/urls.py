from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('categories/<str:name>', blog_view, name='categories'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('newsletter',blog_newsletter_view,name='newsletter'),
    path('search/', blog_search, name='search'),
    path('test',test)
]