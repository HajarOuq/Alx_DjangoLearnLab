from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from .models import Book
from .models import Library
from .views import list_books


# ------------------------------
# Function-Based View (FBV)
# ------------------------------
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# ------------------------------
# Class-Based View (CBV)
# ------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
