from rest_framework import permissions

class KekoPermmission(permissions.BasePermission):
	message = "No eres Keko"

	def has_permission(self,request,view):


		if request.method == "GET" and request.user.email == "buzz@hotmail.com":
			return True
		else:
			return False



