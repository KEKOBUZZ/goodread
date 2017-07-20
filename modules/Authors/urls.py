from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', AuthorList.as_view()),
]
