from django.contrib import admin
from .models import Contact,Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['id' , 'name' , 'email' , 'subject' , 'created_date' , 'updated_date']
    empty_value_display = '-empty-'
    search_fields = ['email','message']



admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)