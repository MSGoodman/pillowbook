from django.conf.urls import url, include
from .drf_public_views import *

urlpatterns = [
	url(r'^task$', TaskList.as_view()),
	url(r'^task/(?P<date>\d{4}-\d{2}-\d{2})$', TaskList.as_view()),
]