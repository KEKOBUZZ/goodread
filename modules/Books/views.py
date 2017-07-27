#from django.shortcuts import render
from .models import Book
from rest_framework import generics,filters
#from .serializers import * BookSerializer
from .serializers import * 
from rest_framework.permissions import IsAdminUser #prpteger vista a solo superusuarios
from .permissions import KekoPermmission
import django_filters.rest_framework
# Create your views here.

#generic views / templates de codigo 

class BookList(generics.ListCreateAPIView):
	#permission_classes = (IsAdminUser,)#solo los superusuarios pueden entrar 
	#permission_classes = (KekoPermmission,)
	serializer_class = BookSerializer
	queryset = Book.objects.all()
	filter_backends = (filters.SearchFilter,
	django_filters.rest_framework.DjangoFilterBackend)
	filter_fields = ('name','ISBN','author','lit_genre')
	search_fields = ('name','ISBN','summary')

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BookSerializer
	queryset = Book.objects.all()

class BookAuthorList(generics.ListAPIView):
	serializer_class = BookAuthorSerializer
	queryset = Book.objects.all()