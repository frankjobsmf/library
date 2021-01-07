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

#serializers estructura
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
            'stock'
        )

class BookForRentBookSerializer(serializers.ModelSerializer):
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
            'published'
        )

class RentBookSerializer(serializers.ModelSerializer):
    book = BookForRentBookSerializer()
    reader = ReaderSerializer()

    class Meta:
        model = RentBook
        fields = (
            'id',
            'reader',
            'book',
            'date_rent',
            'date_return',
            'rented'
        )

#serializadores tipo formulario
###############################################################
#author id serializer
class AuthorIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

#book id serializer
class BookIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

#category id serializer
class CategoryIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

#create rent book
class CreateRentBookSerializer(serializers.Serializer):
    #reader = ReaderIdSerializer()
    books = BookIdSerializer(many=True)

class CreateBookSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    author = AuthorIdSerializer()
    category = CategoryIdSerializer()
    published = serializers.DateField()
    rented = serializers.BooleanField()

#actualizar stock libro
class StockBookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    stock = serializers.IntegerField()


#devolver libro
class ReturnedBookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book = serializers.IntegerField()