from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from datetime import timezone, timedelta
from django.db.models import Sum, Avg
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, Http404

from django.core import serializers

from .models import *

def app_login(request):
    if request.POST:
        user = authenticate(username = request.POST['email'], password = request.POST['password'])
        response = HttpResponse()
        if user is None:
            return render(request, 'login_page.html', {'error': 'Incorrect login details' })
        else:
            login(request, user)
            return HttpResponseRedirect('/app/')
    else:
        return render(request, 'login_page.html', {})
    raise Http404('Something Is Not Set Right')

def module(request):
    return render(request, 'modules.html', {})

def index(request):
# LAST SEVEN DAYS
    last_seven_days = []
    for i in range(0, 7):
        last_seven_days.append({})
        date = datetime.now().date() - timedelta(i)
    
        last_seven_days[i]['Date'] = date

        # Overview
        overview = Overview.objects.filter(date=date)
        last_seven_days[i]['Overview'] = Overview.objects.filter(date=date)

        # Health
        sleep = Sleep.objects.filter(date=date)
        last_seven_days[i]['Sleep'] = sleep if sleep else None
        last_seven_days[i]['Weight'] = WeightExercise.objects.filter(date=date)
        last_seven_days[i]['Cardio'] = CardioExercise.objects.filter(date=date)
        
        foods = Food.objects.filter(date=date)
        day_food_rating = foods.aggregate(Avg('rating'))['rating__avg']
        day_food_calories = foods.aggregate(Sum('calories'))['calories__sum']
        last_seven_days[i]['FoodRating'] = day_food_rating
        last_seven_days[i]['FoodCalories'] = day_food_calories
        
        last_seven_days[i]['Toilet'] = Toilet.objects.filter(date=date)
        last_seven_days[i]['Period'] = Period.objects.filter(date=date)
        last_seven_days[i]['Sex'] = Sex.objects.filter(date=date)

        # Productivity
        moneys = Money.objects.filter(date=date)
        day_money = moneys.aggregate(Sum('amount'))
        last_seven_days[i]['Money'] = moneys
        last_seven_days[i]['MoneyTotal'] = day_money

        last_seven_days[i]['ToDo'] = ToDo.objects.filter(date=date)
        last_seven_days[i]['Learn'] = Learning.objects.filter(date=date)
        last_seven_days[i]['Memory'] = Study.objects.filter(date=date)

        # Art
        lit = Literature.objects.filter(date=date)
        last_seven_days[i]['Literature'] = lit
        #last_seven_days[i]['Literature'] = serializers.serialize("json", lit)


        last_seven_days[i]['Film'] = Film.objects.filter(date=date)
        last_seven_days[i]['Television'] = Television.objects.filter(date=date)
        last_seven_days[i]['BoardGame'] = BoardGame.objects.filter(date=date)
        last_seven_days[i]['VideoGame'] = VideoGame.objects.filter(date=date)
        last_seven_days[i]['Music'] = Music.objects.filter(date=date)
        last_seven_days[i]['Podcast'] = Podcast.objects.filter(date=date)
        last_seven_days[i]['Beer'] = Beer.objects.filter(date=date)
        last_seven_days[i]['Wine'] = Wine.objects.filter(date=date)
        last_seven_days[i]['Cheese'] = Cheese.objects.filter(date=date)
    
    context = {
        'last_seven_days':last_seven_days,
        'buttons': serializers.serialize("json", ModuleButton.objects.all()),
    }

    return render(request, 'indexRouter.html', context)

def overview(request):
    return render(request, 'overview.html', {'title':'Overview'})

def sleep(request):
    return render(request, 'sleep.html', {'title':'Sleep'})

def weight(request):
    return render(request, 'weight.html', {'title': 'Weight'})

def cardio(request):
    return render(request, 'cardio.html', {'title': 'Cardio'})

def food(request):
    return render(request, 'food.html', {'title': 'Food'})

def toilet(request):
    return render(request, 'toilet.html', {'title':'Toilet'})

def sex(request):
    return render(request, 'sex.html', {'title':'Sex'})

def period(request):
    return render(request, 'period.html', {'title':'Period'})

def learning(request):
    return render(request, 'learning.html', {'title':'Learning'})

def money(request):
    return render(request, 'money.html', {'title':'Money'})

def study(request):
    return render(request, 'study.html', {'title':'Study'})

def todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/')
    else:
        form = ToDoForm()

    data = {'form': form, 'title':'To-Do', 
    'pursuits': serializers.serialize("json", Pursuit.objects.all()) }

    print(serializers.serialize("json", Pursuit.objects.all()))
    return render(request, 'todo.html', data)

def project(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/')
    else:
        form = ToDoForm()

    data = {
        'projects': serializers.serialize("json", Project.objects.all()) 
    }

    return render(request, 'projects.html', data)

def quiz(request):
    data = {
        'quizzes': serializers.serialize("json", Quiz.objects.all()) 
    }

    return render(request, 'quizzes.html', data)

def pursuit(request):
    return render(request, 'pursuits.html', {})

def pursuitprogress(request):
    return render(request, 'pursuitprogress.html', {})

def weightExercise(request):
    return render(request, 'weightExercises.html', {})

def cardioExercise(request):
    return render(request, 'cardioExercises.html', {})

def literature(request):
    return render(request, 'literature.html', {'title':'Literature'})

def film(request):
    return render(request, 'film.html', {'title':'Film'})

def television(request):
    return render(request, 'television.html', {'title':'Television'})

def boardgame(request):
    return render(request, 'boardgame.html', {'title':'Board Game'})

def videogame(request):
    return render(request, 'videogames.html', {'title':'Video Game'})

def music(request):
    return render(request, 'music.html', {'title':'Music'})

def podcast(request):
    return render(request, 'podcast.html', {'title':'Podcast'})

def beer(request):
    return render(request, 'beer.html', {'title':'Beer'})

def wine(request):
    return render(request, 'wine.html', {'title':'Wine'})

def cheese(request):
    return render(request, 'cheese.html', {'title':'Cheese'})


def foodItem(request):
    return render(request, 'foodItems.html', {'title': 'Food Items'})

def recipe(request):
    return render(request, 'recipes.html', {'title': 'Recipes'})

def cooking(request):
    return render(request, 'cooking.html', {'title': 'Cooking'})

def grocerypurchase(request):
    return render(request, 'grocerypurchase.html', {'title': 'Groceries'})

def meal(request):
    return render(request, 'meal.html', {'title': 'Meals'})

def travel(request):
    return render(request, 'travel.html', {'title': 'Travels'})

def filmwish(request):
    return render(request, 'filmwish.html', {'title': 'Films To Watch'})