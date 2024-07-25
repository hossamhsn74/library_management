from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('borrow-records/',
         views.BorrowRecordListCreateView.as_view(), name='borrowrecord-list'),
    path('borrow-records/<int:pk>/',
         views.BorrowRecordDetailView.as_view(), name='borrowrecord-detail'),
]
