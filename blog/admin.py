from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'title', 'published')
    search_fields = ('title', 'content')
    date_hierarchy = ('published')
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
