from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['id','title' , 'author', 'counted_views' , 'status' , 'created_date' , 'publish_date']
    empty_value_display = '-empty-'
    list_filter = ['status']
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['id', 'post', 'author', 'created_date', 'approved']
    empty_value_display = '-empty-'
    list_filter = ['approved','post']
    search_fields = ['content']

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)