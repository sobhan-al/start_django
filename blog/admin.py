from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['id','title' , 'counted_views' , 'status' , 'created_date' , 'publish_date']
    empty_value_display = '-empty-'
    list_filter = ['status']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)