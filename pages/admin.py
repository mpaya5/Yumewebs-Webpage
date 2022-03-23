from django.contrib import admin
from .models import Page
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Page, PageAdmin)