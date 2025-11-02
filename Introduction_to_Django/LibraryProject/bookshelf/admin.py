from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by in the right sidebar
    list_filter = ('publication_year', 'author')

    # Search functionality for quick lookups
    search_fields = ('title', 'author')
