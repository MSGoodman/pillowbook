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

class ModuleButtonList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ModuleButtonSerializer
	
	def get_queryset(self):
		return ModuleButton.objects.filter(user=self.request.user)

class ModuleButtonDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ModuleButtonSerializer
	def get_queryset(self): return ModuleButton.objects.filter(user=self.request.user)

class OverviewList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = OverviewSerializer

	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Overview.objects.filter(date=this_date, user=self.request.user)
		else:
			return Overview.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class OverviewDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = OverviewSerializer
	def get_queryset(self): return Overview.objects.filter(user=self.request.user)
	
	def perform_update(self, serializer):
		sent_user = self.request.data['user']
		item_user = Overview.objects.get(pk = self.request.data['id']).user.pk
		if (sent_user != item_user): raise PermissionDenied
		serializer.save()
		return Response(serializer.data)

class SleepList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = SleepSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Sleep.objects.filter(date=this_date, user=self.request.user)
		else:
			return Sleep.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class SleepDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = SleepSerializer
	def get_queryset(self): return Sleep.objects.filter(user=self.request.user)

class WeightList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = WeightSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return WeightExercise.objects.filter(date=this_date, user=self.request.user)
		else:
			return WeightExercise.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class WeightDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = WeightSerializer
	def get_queryset(self): return WeightExercise.objects.filter(user=self.request.user)

class WeightTypeList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = WeightTypeSerializer
	def get_queryset(self): return WeightExerciseType.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class WeightTypeDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = WeightTypeSerializer
	def get_queryset(self): return WeightExerciseType.objects.filter(user=self.request.user)

class CardioList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CardioSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return CardioExercise.objects.filter(date=this_date, user=self.request.user)
		else:
			return CardioExercise.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class CardioDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CardioSerializer
	def get_queryset(self): return CardioExercise.objects.filter(user=self.request.user)

class CardioTypeList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CardioTypeSerializer
	def get_queryset(self): return CardioExerciseType.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class CardioTypeDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CardioTypeSerializer
	def get_queryset(self): return CardioExerciseType.objects.filter(user=self.request.user)

class FoodList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FoodSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Food.objects.filter(date=this_date, user=self.request.user)
		else:
			return Food.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class FoodDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FoodSerializer
	def get_queryset(self): return Food.objects.filter(user=self.request.user)

class ToiletList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ToiletSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Toilet.objects.filter(date=this_date, user=self.request.user)
		else:
			return Toilet.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class ToiletDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ToiletSerializer
	def get_queryset(self): return Toilet.objects.filter(user=self.request.user)

class SexList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = SexSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Sex.objects.filter(date=this_date, user=self.request.user)
		else:
			return Sex.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class SexDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = SexSerializer
	def get_queryset(self): return Sex.objects.filter(user=self.request.user)

class PeriodList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PeriodSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Period.objects.filter(date=this_date, user=self.request.user)
		else:
			return Period.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class PeriodDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PeriodSerializer
	def get_queryset(self): return Period.objects.filter(user=self.request.user)

class LearningList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = LearningSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Learning.objects.filter(date=this_date, user=self.request.user)
		else:
			return Learning.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class LearningDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = LearningSerializer
	def get_queryset(self): return Learning.objects.filter(user=self.request.user)

class StudyList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = StudySerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Study.objects.filter(date=this_date, user=self.request.user)
		else:
			return Study.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class StudyDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = StudySerializer
	def get_queryset(self): return Study.objects.filter(user=self.request.user)

class QuizList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = QuizSerializer
	def get_queryset(self): return Quiz.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class QuizDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = QuizSerializer
	def get_queryset(self): return Quiz.objects.filter(user=self.request.user)

class MoneyList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = MoneySerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Money.objects.filter(date=this_date, user=self.request.user)
		else:
			return Money.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class MoneyDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = MoneySerializer
	def get_queryset(self): return Money.objects.filter(user=self.request.user)

class ToDoList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ToDoSerializer
	def get_queryset(self): 
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			todo_q = Q(create_time__date__lte = this_date.date()) & (Q(finish_time__date__gte = this_date.date()) | Q(finish_time__isnull=True)) & Q(user=self.request.user)
			todos = ToDo.objects.filter(create_time__date__lte = this_date.date(), finish_time__date__gte = this_date.date())
			return ToDo.objects.filter(todo_q) # ToDo.objects.filter(date=this_date, user=self.request.user) # 
		else:
			return ToDo.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)
	'''
	def create(self, request):
		serializer = self.get_serializer(data=request.data)

		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		item = ToDo.objects.create(
			date=serializer.data['date'],
			name=serializer.data['name'],
			pursuit=serializer.data['pursuit'],
			status=serializer.data['status'],
			rank=ToDo.objects.aggregate(Max('rank'))+1
		)

		result = ToDoSerializer(item)
		return Response(result.data, status=status.HTTP_201_CREATED)
'''

class ToDoDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ToDoSerializer
	def get_queryset(self): return ToDo.objects.filter(user=self.request.user)

class PursuitList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PursuitSerializer
	def get_queryset(self): return Pursuit.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class PursuitDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PursuitSerializer
	def get_queryset(self): return Pursuit.objects.filter(user=self.request.user)

class PursuitProgressList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PursuitProgressSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return PursuitProgress.objects.filter(date=this_date, user=self.request.user)
		else:
			return PursuitProgress.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class PursuitProgressDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PursuitProgressSerializer
	def get_queryset(self): return PursuitProgress.objects.filter(user=self.request.user)

class ProjectList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ProjectSerializer
	def get_queryset(self): return Project.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = ProjectSerializer
	def get_queryset(self): return Project.objects.filter(user=self.request.user)

class LiteratureList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = LiteratureSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Literature.objects.filter(date=this_date, user=self.request.user)
		else:
			return Literature.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class LiteratureDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = LiteratureSerializer
	def get_queryset(self): return Literature.objects.filter(user=self.request.user)

class FilmList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FilmSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Film.objects.filter(date=this_date, user=self.request.user)
		else:
			return Film.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class FilmDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FilmSerializer
	def get_queryset(self): return Film.objects.filter(user=self.request.user)

class TelevisionList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = TelevisionSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Television.objects.filter(date=this_date, user=self.request.user)
		else:
			return Television.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class TelevisionDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = TelevisionSerializer
	def get_queryset(self): return Television.objects.filter(user=self.request.user)

class BoardGameList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = BoardGameSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return BoardGame.objects.filter(date=this_date, user=self.request.user)
		else:
			return BoardGame.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class BoardGameDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = BoardGameSerializer
	def get_queryset(self): return BoardGame.objects.filter(user=self.request.user)

class VideoGameList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = VideoGameSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return VideoGame.objects.filter(date=this_date, user=self.request.user)
		else:
			return VideoGame.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class VideoGameDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = VideoGameSerializer
	def get_queryset(self): return VideoGame.objects.filter(user=self.request.user)

class MusicList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = MusicSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Music.objects.filter(date=this_date, user=self.request.user)
		else:
			return Music.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class MusicDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = MusicSerializer
	def get_queryset(self): return Music.objects.filter(user=self.request.user)

class PodcastList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PodcastSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Podcast.objects.filter(date=this_date, user=self.request.user)
		else:
			return Podcast.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class PodcastDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = PodcastSerializer
	def get_queryset(self): return Podcast.objects.filter(user=self.request.user)

class BeerList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = BeerSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Beer.objects.filter(date=this_date, user=self.request.user)
		else:
			return Beer.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class BeerDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = BeerSerializer
	def get_queryset(self): return Beer.objects.filter(user=self.request.user)

class WineList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = WineSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Wine.objects.filter(date=this_date, user=self.request.user)
		else:
			return Wine.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class WineDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = WineSerializer
	def get_queryset(self): return Wine.objects.filter(user=self.request.user)

class CheeseList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CheeseSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Cheese.objects.filter(date=this_date, user=self.request.user)
		else:
			return Cheese.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class CheeseDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CheeseSerializer
	def get_queryset(self): return Cheese.objects.filter(user=self.request.user)


class FoodItemList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FoodItemSerializer
	def get_queryset(self): return FoodItem.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class FoodItemDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FoodItemSerializer
	def get_queryset(self): return FoodItem.objects.filter(user=self.request.user)

class RecipeList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = RecipeSerializer
	def get_queryset(self): return Recipe.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class RecipeDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = RecipeSerializer
	def get_queryset(self): return Recipe.objects.filter(user=self.request.user)

class RecipeIngredientsList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = RecipeIngredientsSerializer
	def get_queryset(self): return RecipeIngredients.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class RecipeIngredientsDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = RecipeIngredientsSerializer
	def get_queryset(self): return RecipeIngredients.objects.filter(user=self.request.user)

class CookingList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CookingSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Cooking.objects.filter(date=this_date, user=self.request.user)
		else:
			return Cooking.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class CookingDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = CookingSerializer
	def get_queryset(self): return Cooking.objects.filter(user=self.request.user)

class GroceryPurchaseList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = GroceryPurchaseSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return GroceryPurchase.objects.filter(date=this_date, user=self.request.user)
		else:
			return GroceryPurchase.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)
	
class GroceryPurchaseDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = GroceryPurchaseSerializer
	def get_queryset(self): return GroceryPurchase.objects.filter(user=self.request.user)

class MealList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = MealSerializer
	def get_queryset(self):  
		this_date_string = self.kwargs.get('date')
		if (this_date_string):
			this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
			return Meal.objects.filter(date=this_date, user=self.request.user)
		else:
			return Meal.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class MealDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = MealSerializer
	def get_queryset(self): return Meal.objects.filter(user=self.request.user)

class TravelList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = TravelSerializer
	def get_queryset(self):  
			this_date_string = self.kwargs.get('date')
			if (this_date_string):
				this_date = datetime.strptime(this_date_string, '%Y-%m-%d')
				return Travel.objects.filter(date=this_date, user=self.request.user)
			else:
				return Travel.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class TravelDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = TravelSerializer
	def get_queryset(self): return Travel.objects.filter(user=self.request.user)

class FilmWishList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FilmWishSerializer
	def get_queryset(self): return FilmWish.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class FilmWishDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FilmWishSerializer
	def get_queryset(self): return FilmWish.objects.filter(user=self.request.user)

class BoardGameWishList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = BoardGameWishSerializer
	def get_queryset(self): return BoardGameWish.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class BoardGameWishDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = BoardGameWishSerializer
	def get_queryset(self): return BoardGameWish.objects.filter(user=self.request.user)

class LiteratureWishList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = LiteratureWishSerializer
	def get_queryset(self): return LiteratureWish.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)
		return Response(serializer.data)

class LiteratureWishDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = LiteratureWishSerializer
	def get_queryset(self): return LiteratureWish.objects.filter(user=self.request.user)

class TodayDataFilled(APIView):
	def get(self, request, format=None):
		return Response({
			'Overview': Overview.objects.filter(date=datetime.now().date()).count(),
			'Sleep': Sleep.objects.filter(date=datetime.now().date()).count(),
			'Weight': WeightExercise.objects.filter(date=datetime.now().date()).count(),
			'Cardio': CardioExercise.objects.filter(date=datetime.now().date()).count(),
			'Food': Food.objects.filter(date=datetime.now().date()).count(),
			'Toilet': Toilet.objects.filter(date=datetime.now().date()).count(),
			'Sex': Sex.objects.filter(date=datetime.now().date()).count(),
			'Period': Period.objects.filter(date=datetime.now().date()).count(),
			'Learning': Learning.objects.filter(date=datetime.now().date()).count(),
			'Money': Money.objects.filter(date=datetime.now().date()).count(),
			'Study': Study.objects.filter(date=datetime.now().date()).count(),
			'To-Do': ToDo.objects.filter(date=datetime.now().date()).count(),
			'Literature': Literature.objects.filter(date=datetime.now().date()).count(),
			'Film': Film.objects.filter(date=datetime.now().date()).count(),
			'Television': Television.objects.filter(date=datetime.now().date()).count(),
			'BoardGame': BoardGame.objects.filter(date=datetime.now().date()).count(),
			'VideoGame': VideoGame.objects.filter(date=datetime.now().date()).count(),
			'Music': Music.objects.filter(date=datetime.now().date()).count(),
			'Podcast': Podcast.objects.filter(date=datetime.now().date()).count(),
			'Beer': Beer.objects.filter(date=datetime.now().date()).count(),
			'Wine': Wine.objects.filter(date=datetime.now().date()).count(),
			'Cheese': Cheese.objects.filter(date=datetime.now().date()).count(),
			'Pursuit Progress': PursuitProgress.objects.filter(date=datetime.now().date()).count(),
		})
