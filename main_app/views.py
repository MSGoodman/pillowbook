from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from datetime import timezone, timedelta
from django.db.models import Sum, Avg
from django.contrib.auth import authenticate, login, logout
from custom_user.forms import EmailUserCreationForm
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
            return HttpResponseRedirect('/')
    else:
        return render(request, 'login_page.html', {})
    raise Http404('Something Is Not Set Right')

def make_new_user_module_buttons(user_instance):
    print(user_instance)
    print("MAKING BUTTONS")
    ModuleButton.objects.create(name='Overview',url_name='overview',icon_font_awesome='clipboard-list',user=user_instance)
    print("MADE ONE")
    ModuleButton.objects.create(name='Sleep',url_name='sleep',icon_font_awesome='bed',user=user_instance)
    ModuleButton.objects.create(name='Weight',url_name='weight',icon_font_awesome='dumbbell',user=user_instance)
    ModuleButton.objects.create(name='Cardio',url_name='cardio',icon_font_awesome='walking',user=user_instance)
    ModuleButton.objects.create(name='Toilet',url_name='toilet',icon_font_awesome='poo',user=user_instance)
    ModuleButton.objects.create(name='Sex',url_name='sex',icon_font_awesome='heart',user=user_instance)
    ModuleButton.objects.create(name='Period',url_name='period',icon_font_awesome='tint',user=user_instance)
    ModuleButton.objects.create(name='Learning',url_name='learning',icon_font_awesome='graduation-cap',user=user_instance)
    ModuleButton.objects.create(name='Money',url_name='money',icon_font_awesome='money-check-alt',user=user_instance)
    ModuleButton.objects.create(name='Study',url_name='study',icon_font_awesome='school',user=user_instance)
    ModuleButton.objects.create(name='ToDo',url_name='todo',icon_font_awesome='tasks',user=user_instance)
    ModuleButton.objects.create(name='Literature',url_name='literature',icon_font_awesome='book',user=user_instance)
    ModuleButton.objects.create(name='Film',url_name='film',icon_font_awesome='video',user=user_instance)
    ModuleButton.objects.create(name='Television',url_name='television',icon_font_awesome='tv',user=user_instance)
    ModuleButton.objects.create(name='Board Games',url_name='boardgame',icon_font_awesome='dice',user=user_instance)
    ModuleButton.objects.create(name='Video Games',url_name='videogame',icon_font_awesome='gamepad',user=user_instance)
    ModuleButton.objects.create(name='Music',url_name='music',icon_font_awesome='music',user=user_instance)
    ModuleButton.objects.create(name='Podcast',url_name='podcast',icon_font_awesome='podcast',user=user_instance)
    ModuleButton.objects.create(name='Beer',url_name='beer',icon_font_awesome='beer',user=user_instance)
    ModuleButton.objects.create(name='Wine',url_name='wine',icon_font_awesome='wine-glass',user=user_instance)
    ModuleButton.objects.create(name='Cheese',url_name='cheese',icon_font_awesome='hockey-puck',user=user_instance)
    ModuleButton.objects.create(name='Pursuit Progress',url_name='pursuitprogress',icon_font_awesome='angle-double-right',user=user_instance)
    ModuleButton.objects.create(name='Cooking',url_name='cooking',icon_font_awesome='concierge-bell',user=user_instance)
    ModuleButton.objects.create(name='Groceries',url_name='grocerypurchase',icon_font_awesome='cart-plus',user=user_instance)
    ModuleButton.objects.create(name='Meals',url_name='meal',icon_font_awesome='utensils',user=user_instance)
    ModuleButton.objects.create(name='Travel',url_name='travel',icon_font_awesome='globe-americas',user=user_instance)

def app_signup(request):
    if request.POST:
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            # Make User
            new_user = User.objects.create_user(email, pass1)
            user = authenticate(email=email, password=pass1)
            # Make Module Buttons
            make_new_user_module_buttons(new_user)
        if user is None:
            return render(request, 'signup.html', {'error': 'User could not be created' })
        else:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        return render(request, 'signup.html', {})
    raise Http404('Something Is Not Set Right')


    return render(request, 'signup.html', {'form':EmailUserCreationForm()})
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        print(form, form.is_valid())
        if form.is_valid():
            return render(request, 'indexRouter.html', {})
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            print(email, raw_password)
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('app')
    else:
        form = EmailUserCreationForm()
    return render(request, 'signup.html', {'form': form})

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