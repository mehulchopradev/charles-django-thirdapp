from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from libapi.serializers import BookSerializer, AuthorSerializer, ContactUsSerializer
from libapi.models import Book, Author

# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorCreateListView(ListCreateAPIView):
    serializer_class = AuthorSerializer
    # queryset = Author.objects.order_by('-ratings')
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        query_params = self.request.query_params
        if 'gender' in query_params:
            return Author.objects.filter(gender=query_params['gender']).order_by('-ratings')
        else:
            return Author.objects.order_by('-ratings')

class AuthorCreateView(CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)

class AuthorListView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.order_by('-ratings')
    permission_classes = (IsAuthenticated,)

class ContactUsView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            cleaned_data = serializer.data
            print(cleaned_data)
            return Response({"success": True})
        else:
            return Response({"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "Invalid username or password"}, status=HTTP_401_UNAUTHORIZED)

'''class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookRetrieve(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()'''
