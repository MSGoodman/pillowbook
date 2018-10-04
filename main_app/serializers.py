from rest_framework import serializers
from django.conf import settings
from urllib.parse import urljoin
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from rest_framework import serializers

from .models import *

class DiarySerializer(serializers.ModelSerializer):
	class Meta:
		model = Diary
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class SleepSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sleep
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):
	class Meta:
		model = WeightExercise
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class CardioSerializer(serializers.ModelSerializer):
	class Meta:
		model = CardioExercise
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class WeightTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = WeightExerciseType
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class CardioTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CardioExerciseType
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Food
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class ToiletSerializer(serializers.ModelSerializer):
	class Meta:
		model = Toilet
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class SexSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sex
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
	class Meta:
		model = Period
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class LearningSerializer(serializers.ModelSerializer):
	class Meta:
		model = Learning
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class StudySerializer(serializers.ModelSerializer):
	class Meta:
		model = Study
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class ToDoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class PursuitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pursuit
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class PursuitProgressSerializer(serializers.ModelSerializer):
	class Meta:
		model = PursuitProgress
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class MoneySerializer(serializers.ModelSerializer):
	class Meta:
		model = Money
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class LiteratureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Literature
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
	class Meta:
		model = Film
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class TelevisionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Television
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class BoardGameSerializer(serializers.ModelSerializer):
	class Meta:
		model = BoardGame
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class VideoGameSerializer(serializers.ModelSerializer):
	class Meta:
		model = VideoGame
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Music
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
	class Meta:
		model = Podcast
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class BeerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Beer
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class WineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Wine
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class CheeseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cheese
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = FoodItem
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class RecipeIngredientsSerializer(serializers.ModelSerializer):
	class Meta:
		model = RecipeIngredients
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
	ingredients = serializers.SerializerMethodField()

	def get_ingredients(self, obj):
		qset = RecipeIngredients.objects.filter(recipe=obj)
		return [RecipeIngredientsSerializer(i).data for i in qset]

	class Meta:
		model = Recipe
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class CookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cooking
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class GroceryPurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = GroceryPurchase
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
	recipes = RecipeSerializer(many=True, read_only=True, required=False)

	class Meta:
		model = Meal
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Travel
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class FilmWishSerializer(TaggitSerializer, serializers.ModelSerializer):
	class Meta:
		model = FilmWish
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class BoardGameWishSerializer(TaggitSerializer, serializers.ModelSerializer):
	class Meta:
		model = BoardGameWish
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class LiteratureWishSerializer(TaggitSerializer, serializers.ModelSerializer):
	class Meta:
		model = LiteratureWish
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'

class ModuleButtonSerializer(serializers.ModelSerializer):
	class Meta:
		model = ModuleButton
		extra_kwargs = { 'user': {'default': serializers.CreateOnlyDefault(serializers.CurrentUserDefault())} } 
		fields = '__all__'