# Django ORM CRUD Operations for Book Model

This document demonstrates the complete implementation of the **Book** model within the `bookshelf` app and the execution of all CRUD (Create, Retrieve, Update, Delete) operations through Django’s ORM.

---

## 🧱 1. Book Model Definition (`bookshelf/models.py`)

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
