from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_on', 'updated_on']
    fields = [
        ('author', 'slug', 'status'),
        'title',
        'post',
    ]
    list_filter = ("status",)
    search_fields = ['title', 'content']
    readonly_fields = ['slug']


admin.site.register(Blog, BlogAdmin)