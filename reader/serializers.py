#rest_framework
from rest_framework import serializers

#authenticate
from django.contrib.auth import authenticate

#model
from .models import Reader

#serializers
class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = (
            'id',
            'first_name',
            'last_name',
            'email'
        )

#registro reader
class RegisterReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = (
            'id',
            'username',
            'email',
            'password'
        )

        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    #creacion
    def create(self, validate_data):
        reader = Reader.objects.create_user(
            validate_data['username'],
            validate_data['email'],
            validate_data['password']
        )
        return reader


#login reader
class LoginReaderSerializer(serializer.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_data(self, data):
        reader = authenticate(**data)

        if reader and reader.is_active:
            return user
        raise serializers.ValidationError("Error de credenciales")
        
