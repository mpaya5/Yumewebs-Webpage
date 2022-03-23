from django.contrib import admin
from .models import Work

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title', 'content')

admin.site.register(Work, WorkAdmin)