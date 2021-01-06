from django.urls import path

#views
from .views import (
    ListBooksAPI,
    ListBookByTitleAPI,
    ListBookByDateRangeAPI,
    ListBookByAuthorAPI,
    ListBookByCategoryAPI,
    ListRentBookAPI,
    CreateRentaBookAPI,
    CreateBookAPI,
    ListRentBookByReaderAPI,
    UpdateStockBookAPI,
    UpdateRentBookReturnedAPI,
)

urlpatterns = [
    path('books', ListBooksAPI.as_view(), name='books'),
    path('find-book-title', ListBookByTitleAPI.as_view(), name='find-book-title'),
    path('find-book-date', ListBookByDateRangeAPI.as_view(), name='find-book-date'),
    path('find-book-author', ListBookByAuthorAPI.as_view(), name='find-book-author'),
    path('find-book-category', ListBookByCategoryAPI.as_view(), name='find-book-category'),
    path('rent-book', CreateRentaBookAPI.as_view(), name='rent-book'),
    path('list-rent-book', ListRentBookAPI.as_view(), name='list-rent-book'),
    path('book-create', CreateBookAPI.as_view(), name='book-create'),
    path('find-rent-book-reader', ListRentBookByReaderAPI.as_view(), name='find-rent-book-reader'),
    path('book-update-stock', UpdateStockBookAPI.as_view(), name='book-update-stock'),
    path('rent-book-returned', UpdateRentBookReturnedAPI.as_view(), name='rent-book-returned'),
]

