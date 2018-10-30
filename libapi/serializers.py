from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from libapi.models import Book, Author

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class ContactUsSerializer(Serializer):
    name = serializers.CharField(required=True, max_length=10)
    email = serializers.EmailField(required=True)
    mobile = serializers.CharField(required=False, max_length=10)
