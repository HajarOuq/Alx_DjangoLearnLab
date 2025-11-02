# Django Admin Configuration for the Book Model

## 🎯 Objective
Gain practical experience with the Django admin interface by configuring the admin to manage the **Book** model within the `bookshelf` app.  
This setup allows administrators to easily add, view, edit, and delete books through the Django Admin UI.

---

## 🧱 1. Book Model (bookshelf/models.py)

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
