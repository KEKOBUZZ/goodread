from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BookList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', BookDetail.as_view()), #P = parametro, primary key pueden pasar un numero entero positivo el que sea
    url(r'^authors/$', BookAuthorList.as_view()),
]

#http://localhost:8000/api/v1/books/authors/