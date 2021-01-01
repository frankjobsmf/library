from django.urls import path

#views
from .views import (
    ListBooksAPI,
    ListBookByTitleAPI,
    ListBookByDateRangeAPI,
    ListBookByAuthorAPI,
    ListBookByCategoryAPI,
    CreateRentaBookAPI,
)

urlpatterns = [
    path('books', ListBooksAPI.as_view(), name='books'),
    path('find-book-title', ListBookByTitleAPI.as_view(), name='find-book-title'),
    path('find-book-date', ListBookByDateRangeAPI.as_view(), name='find-book-date'),
    path('find-book-author', ListBookByAuthorAPI.as_view(), name='find-book-author'),
    path('find-book-category', ListBookByCategoryAPI.as_view(), name='find-book-category'),
    path('rent-book', CreateRentaBookAPI.as_view(), name='rent-book'),
]

