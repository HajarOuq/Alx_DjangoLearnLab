from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
# Read-only access for everyone
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching by text in these fields
    search_fields = ['title', 'author__name']  # note author is FK, use __name

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Only authenticated users can modify data
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


