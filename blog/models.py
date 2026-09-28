from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    categorys = models.ManyToManyField(Category)
    counted_views = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created_date']

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})


class Comment(models.Model):
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )

    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    