from django.contrib import admin

#models
from .models import Author, Book, Category

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)


