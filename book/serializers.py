#rest_framework
from rest_framework import serializers

#models
from .models import (
    Author,
    Book,
    Category
)

#serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'author',
            'category',
            'published',
            'rented'
        )