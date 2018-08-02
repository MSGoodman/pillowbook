from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from datetime import timedelta, datetime
from django.utils import timezone
from django.db.models import Sum, Avg
from django.contrib.auth import authenticate, login, logout
from custom_user.forms import EmailUserCreationForm
from django.http import JsonResponse, Http404

import hashlib
from django.utils.crypto import get_random_string

from django.core import serializers

from .models import *

def app_activate(request, key):
    activation_expired = False
    already_active = False

    try:
        user = User.objects.get(activation_key=key)
    except User.DoesNotExist:
        return render(request, 'activation_page.html', {'error': 'Invalid activation key.'})

    if user.is_active == False:
        if timezone.now() > user.key_expires: # Expired
            activation_expired = True
            id_user = user.id
            return render(request, 'activation_page.html', {'error': 'Your activation link has expired. A new email has been sent.'})
        else: #Activated
            user.is_active = True
            user.save()
            return redirect('login')

    #If user is already active, simply display error message
    else:
        already_active = True #Display : error message
        return render(request, 'activation_page.html', {'error': 'Your account is already activated.'})

def app_login(request):
    if request.POST:

        user_email = User.objects.get(email=request.POST['email'])
        if not user_email.is_active:
            return render(request, 'login_page.html', {'error': 'Sorry! You must activate your account via the link sent to your email address.' })

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
    work_pursuit = Pursuit.objects.create(name='Work',icon='💼',user=user_instance)
    Pursuit.objects.create(name='Fitness',icon='💪',user=user_instance)
    home_pursuit = Pursuit.objects.create(name='Home Improvement',icon='🏠', user=user_instance)
    Project.objects.create(name='That Big Work Project', pursuit=work_pursuit, description='Integrate blockchain-enabled machine-learning AI into decentralized actionable analytics microservices IoT platform for Q1', user=user_instance)
    Project.objects.create(name='Build Porch', pursuit=home_pursuit, description="That porch isn't going to build itself", user=user_instance)
    WeightExerciseType.objects.create(name='Bench Press', user=user_instance)
    WeightExerciseType.objects.create(name='Barbell Row', user=user_instance)
    CardioExerciseType.objects.create(name='Running', user=user_instance)
    CardioExerciseType.objects.create(name='Cycling', user=user_instance)
    FoodItem.objects.create(name='Chicken Breast', serving_size_qty=3.5, serving_size_unit='oz',calories=165,total_fat=3.6,saturated_fat=1,trans_fat=0,cholesterol=85,sodium=74,potassium=250,total_carbs=0,total_sugars=0,added_sugars=0,protein=31, user=user_instance)
    Quiz.objects.create(name='Countries', url='http://mikesgoodman.com/WorldGeographyQuiz/', total_records=201, user=user_instance)
    Quiz.objects.create(name='U.S. States', url='http://mikesgoodman.com/UsGeographyQuiz/', total_records=201, user=user_instance)

def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()

def app_signup(request):
    if request.POST:
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            # Make User
            activation_key = generate_activation_key(email)
            key_expires = datetime.strftime(datetime.utcnow() + timedelta(days=2), "%Y-%m-%d %H:%M:%S")

            new_user = User.objects.create_user(email, pass1,activation_key=activation_key,is_active=False,key_expires=key_expires)
            # Make Module Buttons
            make_new_user_module_buttons(new_user)
        else:
            return render(request, 'signup.html', {'error': "Passwords didn't match"})

        if new_user is None:
            return render(request, 'signup.html', {'error': 'User could not be created' })
        else:
            login(request, new_user)
            return HttpResponseRedirect('/')

    else:
        return render(request, 'signup.html', {})

    raise Http404('Something Is Not Set Right')

def module(request):
    return render(request, 'modules.html', {})

def index(request):
# LAST SEVEN DAYS
    last_seven_days = []
    for i in range(0, 7):
        last_seven_days.append({})
        date = datetime.utcnow().date() - timedelta(i)
    
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

    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')

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