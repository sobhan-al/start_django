from django import template 
from blog.models import Post 
register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def popularposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-counted_views')[:arg]
    return {'posts':posts}
