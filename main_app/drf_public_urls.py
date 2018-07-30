from django.conf.urls import url, include
from .drf_views import *

urlpatterns = [
	url(r'^task/(?P<date>\d{4}-\d{2}-\d{2})$', ToDoList.as_view()),
]