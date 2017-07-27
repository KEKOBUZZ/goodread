from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', AuthorList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', AuthorDetail.as_view()), #P = parametro, primary key pueden pasar un numero entero positivo el que sea
]
