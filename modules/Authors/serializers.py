from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):


	class Meta:
		model = Author
		fields = ("id","name","last_name","nacionality","biography",
			"gender","age","is_alive")

#cuando traiga el objeto lo convierte en diccionrio



