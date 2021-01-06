#python
from datetime import datetime
now = datetime.now()


#rest_framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    GenericAPIView,
    UpdateAPIView,
)

from rest_framework.response import Response
from rest_framework import permissions

#serializers
from .serializers import (
    BookSerializer,
    CreateRentBookSerializer,
    RentBookSerializer,
    CreateBookSerializer,
    StockBookSerializer,
    ReturnedBookSerializer,
)

#models
from .models import (
    Author,
    Book,
    Category,
    RentBook,
)

#LIST
#######################################################################################
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
        author_param = self.request.query_params.get('author', None)
        return Book.objects.FindBookByAuthor(author=author_param)

class ListBookByCategoryAPI(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        category_param = self.request.query_params.get('category', None)
        return Book.objects.FindBookByCategory(category=category_param)

class ListRentBookAPI(ListAPIView): #lista todos las rentas de libros
    serializer_class = RentBookSerializer

    def get_queryset(self):
        return RentBook.objects.all()



class ListRentBookByReaderAPI(ListAPIView): #Listar RentBook por reader
    serializer_class = RentBookSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return RentBook.objects.FindRentBookByReader(id_reader=self.request.user.id)

#CREATE
#######################################################################################

class CreateRentaBookAPI(CreateAPIView):
    serializer_class = CreateRentBookSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def create(self, request, *args, **kwargs):
        serializer = CreateRentBookSerializer(data=request.data)
        #        
        if serializer.is_valid():

            books = serializer.validated_data['books']
            print(books)

            """
            lista que se usara para iterar todos los libros
            que recibamos por JSON
            """
            books_list = []
            
            #
            for b in books:

                #capturamos el id del json
                book = Book.objects.get(id=b['id'])

                #validamos si el libro tiene stock
                if book.stock == 0:
                    return Response({
                        "resp": "Ups, libro no disponible!"
                    })


                #asigando datos al modelo RentBook, para luego crear el registro
                rent_book = RentBook(
                    reader=self.request.user,
                    rented=True,
                    date_rent=now.date(),
                    book=book
                )

                if rent_book.rented is True:
                    print("El libro: " + book.title + ", ha sido rentado con exito!!!")
                    book.stock = book.stock - 1
                    book.save()

                #añadimos nuetra instancia a la lista creada anteriormente
                books_list.append(rent_book)
            
            #debemos hacer uso de la lista, para generar el registro
            RentBook.objects.bulk_create(
                books_list
            )

            return Response({
                "resp": "Genial, se ha generado tu arriendo!"
            })
        #
        return Response({
            "resp": "No pudimos generar tu arriendo :("
        }) 


class CreateBookAPI(CreateAPIView): #se registraran libros
    serializer_class = CreateBookSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateBookSerializer(data=request.data)

        #validamos si el serializer es valido
        if serializer.is_valid():

            #author
            authors = serializer.validated_data['author'] #recuperamos dato del json
            author = Author.objects.get(id=authors['id']) #le pasamos la key id para realizar busqueda

            #category
            categories = serializer.validated_data['category'] #recuperamos dato del json
            category = Category.objects.get(id=categories['id']) #le pasamos la key id para realizar busqueda


            #debug xD
            print("##############################################")
            print(author.name)
            print("##############################################")

            print("##############################################")
            print(category.name)
            print("##############################################")
            
            Book.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data['description'],
                author=author,
                category=category,
                published=serializer.validated_data['published'],
                rented=serializer.validated_data['rented']
            )

            return Response({
                "resp": "Libro agregado con exito!"
            })
        #
        return Response({
            "resp": "No pudimos agregar el libro :("
        })

#UPDATE    
#######################################################################################
class UpdateStockBookAPI(UpdateAPIView):
    serializer_class = StockBookSerializer

    def update(self, request, *args, **kwargs):
        serializer = StockBookSerializer(data=request.data)

        if serializer.is_valid():

            book = Book.objects.get(id=serializer.validated_data['id'])

            book.stock = serializer.validated_data['stock']
            book.save()

            return Response({
                "msg": "Stock actualizado con exito!"
            })
        #
        return Response({
            "msg": "No pudimos actualizar el stock del libro :("
        })

#devolver el libro
class UpdateRentBookReturnedAPI(UpdateAPIView): # EN PROCESO........................................
    serializer_class = ReturnedBookSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def update(self, request, *args, **kwargs):
        serializer = ReturnedBookSerializer(data=request.data)

        if serializer.is_valid():
            
            rentbook_get = RentBook.objects.get(id=serializer.validated_data['id'])
            book_get = Book.objects.get(id=serializer.validated_data['book'])

            print(book_get.title)

            #instancia de rentbook - rentbook_get
            rentbook_get.date_return = now.date() #fecha de devolucion
            rentbook_get.rented = False #este libro ha sido devuelto
            rentbook_get.save()

            #instancia de book - book_get
            book_get.stock = book_get.stock + 1 #al ser devuelto el libro le sumamos 1 al modelo book en stock
            book_get.save()

            return Response({
                "msg": "Libro devuelto!"
            })
        #
        return Response({
            "msg": "Error al devolver el libro"
        })
    