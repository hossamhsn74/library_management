from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from borrow.models import Book, BorrowRecord
from borrow.serializers import BookSerializer, BorrowRecordSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    View to list all books or create a new book.

    * Requires token authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a book.

    * Requires token authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BorrowRecordListCreateView(generics.ListCreateAPIView):
    """
    View to list all borrow records or create a new borrow record.

    * Requires token authentication.
    """
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Handle creating a borrow record, ensuring the book is available.

        * Updates the book's availability status.
        * Raises a validation error if the book is not available.
        """
        book = serializer.validated_data['book']
        if book.available:
            book.available = False
            book.save()
            serializer.save()
        else:
            raise serializers.ValidationError("Book is not available.")


class BorrowRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a borrow record.

    * Requires token authentication.
    """
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Handle updating a borrow record, setting the book's availability if returned.

        * Updates the book's availability status upon return.
        """
        borrow_record = self.get_object()
        if 'return_date' in serializer.validated_data:
            borrow_record.book.available = True
            borrow_record.book.save()
        serializer.save()
