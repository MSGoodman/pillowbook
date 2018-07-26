from django import forms
from .models import *

class OverviewForm(forms.ModelForm):
    class Meta:
        model = Overview
        fields = "__all__"

class SleepForm(forms.ModelForm):
    start_time = forms.TimeField(input_formats=['%I:%M %p'])
    end_time = forms.TimeField(input_formats=['%I:%M %p'])

    class Meta:
        model = Sleep
        fields = "__all__"

class WeightForm(forms.ModelForm):
    start_time = forms.TimeField(input_formats=['%I:%M %p'])
    end_time = forms.TimeField(input_formats=['%I:%M %p'])

    class Meta:
        model = WeightExercise
        fields = "__all__"

class CardioForm(forms.ModelForm):
    start_time = forms.TimeField(input_formats=['%I:%M %p'])
    end_time = forms.TimeField(input_formats=['%I:%M %p'])

    class Meta:
        model = CardioExercise
        fields = "__all__"

class FoodForm(forms.ModelForm):
    eat_time = forms.TimeField(input_formats=['%I:%M %p'])

    class Meta:
        model = Food
        fields = "__all__"

class ToiletForm(forms.ModelForm):
    start_time = forms.TimeField(input_formats=['%I:%M %p'])
    end_time = forms.TimeField(input_formats=['%I:%M %p'])

    class Meta:
        model = Toilet
        fields = "__all__"

class SexForm(forms.ModelForm):
    class Meta:
        model = Sex
        fields = "__all__"

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = "__all__"

class LearningForm(forms.ModelForm):
    class Meta:
        model = Learning
        fields = "__all__"

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = "__all__"

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = "__all__"

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"

class LiteratureForm(forms.ModelForm):
    class Meta:
        model = Literature
        fields = "__all__"

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"

class TelevisionForm(forms.ModelForm):
    class Meta:
        model = Television
        fields = "__all__"

class BoardGameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = "__all__"

class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = "__all__"

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = "__all__"

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = "__all__"

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = "__all__"

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = "__all__"

class CheeseForm(forms.ModelForm):
    class Meta:
        model = Cheese
        fields = "__all__"