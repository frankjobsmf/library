#rest_framework
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
) 

from rest_framework.response import Response
from rest_framework import permissions

#knox
from knox.models import AuthToken

#serializers
from .serializers import (
    ReaderSerializer,
    RegisterReaderSerializer,
    LoginReaderSerializer,
    UpdateReaderSerializer,
)

#models
from .models import Reader

#views
class ListReaderAPI(ListAPIView): #listamos a todos los lectores / usuarios
    serializer_class = ReaderSerializer

    def get_queryset(self):
        return Reader.objects.all()

class RegisterReaderAPI(GenericAPIView): #registro de lectores / usuarios
    serializer_class = RegisterReaderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        #verificamos si los datos recibidos son validos
        serializer.is_valid(raise_exception=True)

        reader = serializer.save()

        return Response({
            "reader": ReaderSerializer(reader, context=self.get_serializer_context()).data
        })

class LoginReaderAPI(GenericAPIView): # login de lectores / usuarios
    serializer_class = LoginReaderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reader = serializer.validated_data
        _, token = AuthToken.objects.create(reader)

        return Response({
            "reader": ReaderSerializer(reader, context=self.get_serializer_context()).data,
            "token": token
        })

class ListReaderAPI(RetrieveAPIView): #listado de informacion del usuario autenticado / lector
    serializer_class = ReaderSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user

class UpdateReaderProfileAPI(UpdateAPIView): #Actualizar la informacion del lector
    serializer_class = UpdateReaderSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def update(self, request, *args, **kwargs):
        serializer = UpdateReaderSerializer(data=request.data)

        if serializer.is_valid():
            #le pasamos el id del usuario conectado
            reader = Reader.objects.get(id=self.request.user.id)

            reader.first_name=serializer.validated_data['first_name']
            reader.last_name=serializer.validated_data['last_name']

            #guardamos
            reader.save()

            return Response({
                "resp": "Perfil modificado con exito :)"
            })
        #
        return Response({
            "resp": "No logramos modificar tu perfil :("
        })
