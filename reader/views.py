#rest_framework
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
) 

from rest_framework.response import Response

#serializers
from .serializers import (
    ReaderSerializer,
    RegisterReaderSerializer
)

#models
from .models import Reader

#views
class ListReaderAPI(ListAPIView): #listamos a todos los lectores / usuarios
    serializer_class = ReaderSerializer

    def get_queryset(self):
        return Reader.objects.all()

class RegisterReaderAPI(GenericAPIView):
    serializer_class = RegisterReaderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        #verificamos si los datos recibidos son validos
        serializer.is_valid(raise_exception=True)

        reader = serializer.save()

        return Response({
            "reader": ReaderSerializer(reader, context=self.get_serializer_context()).data
        })