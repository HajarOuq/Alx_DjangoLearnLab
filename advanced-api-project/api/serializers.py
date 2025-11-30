from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# BookSerializer serializes Book model fields and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Ensure publication_year is not in the future
    def validate_publication_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer serializes Author model and nests related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ["name", "books"]  # Include author name and related books
