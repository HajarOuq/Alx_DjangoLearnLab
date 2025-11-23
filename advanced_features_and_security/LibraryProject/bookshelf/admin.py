from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Fields to filter by in the right sidebar
    list_filter = ('publication_year', 'author')

    # Search functionality for quick lookups
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo")
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo")
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

