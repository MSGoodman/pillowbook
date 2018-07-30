from rest_framework import generics, permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from rest_framework.serializers import ValidationError as DRFValidationError
from pprint import pprint
from django.db.models import Q
from django.db.models import Max
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login, logout

from .models import *

from .serializers import *

# CUSTOM PERMISSIONS
class SecretValidatedPermission(permissions.BasePermission):

	def has_permission(self, request, view):
		secret = request.META.get('HTTP_X_PBSECRET') 
		print(secret)
		return secret

# VIEWS
class TaskList(generics.ListCreateAPIView):
	permission_classes = (permissions.AllowAny, SecretValidatedPermission)
	serializer_class = ToDoSerializer

	def get_queryset(self): 
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			print(this_date.date())
			todo_q = Q(create_time__date__lte = this_date.date()) & (Q(finish_time__date__gte = this_date.date()) | Q(finish_time__isnull=True)) & Q(user=self.request.user)
			todos = ToDo.objects.filter(create_time__date__lte = this_date.date(), finish_time__date__gte = this_date.date())
			return ToDo.objects.filter(todo_q) # ToDo.objects.filter(date=this_date, user=self.request.user) # 
		else:
			return ToDo.objects.filter(pk=100)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)