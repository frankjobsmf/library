#rest_framework
from rest_framework.generics import (
    ListAPIView
)

#serializers
from .serializers import (
    BookSerializer
)

#models
from .models import (
    Author,
    Book,
    Category
)

#views
class ListBooksAPI(ListAPIView): #Devuelve todos los libros
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

class ListBookByTitleAPI(ListAPIView): #devuelve los libros relacionado al parametro entregado por la url
    serializer_class = BookSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        return Book.objects.FindBookByTitle(title_param=title)

class ListBookByDateRangeAPI(ListAPIView): #devuelve todos los libros seleccionados por un rango de fecha
    serializer_class = BookSerializer

    def get_queryset(self):
        date1_param = self.request.query_params.get('date1', None)
        date2_param  = self.request.query_params.get('date2', None)

        return Book.objects.FindBookByDateRange(date1=date1_param, date2=date2_param)


class ListBookByAuthorAPI(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.request.query_params.get('author', None)
        return Book.objects.FindBookByAuthor(author=author)