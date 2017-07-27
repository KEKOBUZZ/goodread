from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Author
from .serializers import AuthorSerializer,AuthorBookSerializer
from django.db.models import Q


#Clases basadas en vistas o "clased base view"

class AuthorList(APIView):
	"""

	get:
	Obtiene todos los autores

	post:
	Crea un nuevo autor


	"""

	def get(self,request):
		#get_data = request.query_params
		#print(get_data)
		gender = request.query_params.get('gender')
		is_alive = request.query_params.get('is_alive')
		nacionality = request.query_params.get('nacionality')
		if (gender or is_alive or nacionality) is not None:
			
			authors = Author.objects.filter(Q(gender__icontains=gender)|
				Q(is_alive=bool(is_alive)) |
				Q(nacionality__icontains=nacionality)
			)
			serializer = AuthorSerializer(author,many=True)
			'''
			authors = Author.objects.filter(**get_data)
			serializer = AuthorSerializer(authors,many=True)
			'''
			return Response(serializer.data,status=status.HTTP_200_OK)
			
		else:
			authors = Author.objects.all()
			serializer = AuthorBookSerializer(authors,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)
		

	def post(self,request):
		serializer = AuthorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#localhost:8000/api/v1/authors/

class AuthorDetail(APIView):
#localhost:8000/api/v1/authors/

	'''
	def _get_author(self,pk): #identificador de funcion privada
		try:
			autor = Author.objects.get(id=pk)
			return autor
		except Author.DoesNotExist:
			raise Http404 
	'''

	def get(self,request,pk):
		#autor = self._get_author(pk)
		autor = get_object_or_404(Author,id=pk)
		serializer = AuthorSerializer(autor)
		return Response(serializer.data,status=status.HTTP_200_OK)

		

	def put(self,request,pk):
		#autor = self._get_author(pk)
		autor = get_object_or_404(Author,id=pk)
		serializer = AuthorSerializer(autor,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk):
		#autor = self._get_author(pk)
		autor = get_object_or_404(Author,id=pk)
		autor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)






