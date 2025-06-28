from django.contrib import admin
from .models import Page, Comment

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'page', 'created_at')
    search_fields = ('author__username', 'content')
    list_filter = ('created_at',)
