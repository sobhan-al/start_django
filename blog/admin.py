from django.contrib import admin
from .models import Post,Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['id','title' , 'author', 'counted_views' , 'status' , 'created_date' , 'publish_date']
    empty_value_display = '-empty-'
    list_filter = ['status']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)