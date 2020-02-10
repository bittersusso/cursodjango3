from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'full_name']
    search_fields = ['title', 'subtitle']
    fields = ('title', 'subtitle')

admin.site.register(Post, PostAdmin)