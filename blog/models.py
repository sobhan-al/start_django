from django.db import models

class Post(models.Model):
    #image
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    #category
    counted_views = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['created_date']

