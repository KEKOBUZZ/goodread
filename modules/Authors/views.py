from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorSerializer



#Clases basadas en vistas o "clased base view"

class AuthorList(APIView):

	def get(self,request):
		authors = Author.objects.all()
		serializer = AuthorSerializer(authors,many=True)
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

	def get(self,request):
		pass

	def post(self,request):
		pass

	def delete(self,request):
		pass




