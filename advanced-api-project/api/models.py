from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Author model represents a book author
class Author(models.Model):
    name = models.CharField(max_length=200)  # Store the author's name

    def __str__(self):
        return self.name


# Book model represents a book written by an Author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )  # Link to Author (one-to-many)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    # Custom validation to prevent future publication years
    def clean(self):
        if self.publication_year > timezone.now().year:
            raise ValidationError("Publication year cannot be in the future.")
