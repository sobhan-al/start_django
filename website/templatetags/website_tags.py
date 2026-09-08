from django import template
from blog.models import Post,Category
register = template.Library()


@register.filter
def slide_contents(text):
    length = len(text)
    if length > 90:
        part1 = text[:60] + '... ' + text[-30:]
    else:
        part1 = text
    return part1    