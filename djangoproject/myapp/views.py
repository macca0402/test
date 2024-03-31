# Create your views here.
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book

@login_required
@api_view(["GET"])
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@login_required
@api_view(["POST"])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@login_required
@api_view(["GET"])
def detail_book(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@login_required
@api_view(["PUT"])
def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)
@login_required
@api_view(["DELETE"])
def delete_book(request,book_id):
    book=Book.objects.get(id=book_id)
    book.delete()
    return Response("Deleted book")