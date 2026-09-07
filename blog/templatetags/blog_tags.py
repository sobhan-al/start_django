from django import template 
from blog.models import Post,Category
register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def popularposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-counted_views')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-categorys-all.html')
def category_counter():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]= posts.filter(categorys=name).count()

    return {'categoryies':cat_dict}
