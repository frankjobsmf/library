#rest_framework
from rest_framework import serializers

#models
from .models import (
    Author,
    Book,
    Category,
    RentBook,
)

#serializer app reader
from reader.serializers import ReaderSerializer, ReaderIdSerializer

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

#book id serializer
class BookIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

#create rent book
class CreateRentBookSerializer(serializers.Serializer):
    #reader = ReaderIdSerializer()
    books = BookIdSerializer(many=True)

