from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_http_methods
from .models import Book
from .forms import BookForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'bookshelf/create_book.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('book_list')

    return render(request, 'bookshelf/edit_book.html', {'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')


# Safe list view (no raw SQL)
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Use ORM which parameterizes queries internally
    q = request.GET.get("q", "").strip()
    if q:
        # Example: use icontains to avoid building SQL strings manually
        books = Book.objects.filter(title__icontains=q)
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books, "query": q})


# Create view using ModelForm to validate input
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})


# Edit view
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
@require_http_methods(["GET", "POST"])
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookshelf:book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Edit"})