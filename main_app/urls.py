from django.conf.urls import url,  include

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),

    url(r'^login$', views.app_login, name='login'),
    url(r'^signup$', views.app_signup, name='signup'),
    url(r'^activate/(?P<key>.+)$', views.app_activate, name='activate'),
    url(r'^user', views.user, name='activate'),

    url(r'^modules$', views.module, name='modules'),
    url(r'^diary/$', views.diary, name='diary'),
	url(r'^diary/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<date>[0-9]+)$', views.diary, name='diary'),

    url(r'^sleep/$', views.sleep, name='sleep'),
    url(r'^sleep/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<date>[0-9]+)$', views.sleep, name='sleep'),
    url(r'^weight/$', views.weight, name='weight'),
    url(r'^cardio/$', views.cardio, name='cardio'),
    url(r'^food/$', views.food, name='food'),
    url(r'^toilet/$', views.toilet, name='toilet'),
    url(r'^sex/$', views.sex, name='sex'),
    url(r'^period/$', views.period, name='period'),

    url(r'^weightExercises/$', views.weightExercise, name='weightExercises'),
    url(r'^cardioExercises/$', views.cardioExercise, name='cardioExercises'),

    url(r'^learning/$', views.learning, name='learning'),
    url(r'^money/$', views.money, name='money'),
    url(r'^study/$', views.study, name='study'),
    url(r'^todo/$', views.todo, name='todo'),
    url(r'^projects/$', views.project, name='project'),
    url(r'^quizzes/$', views.quiz, name='quiz'),
    url(r'^pursuits/$', views.pursuit, name='pursuit'),
    url(r'^pursuitprogress/$', views.pursuitprogress, name='pursuitprogress'),

    url(r'^literature/$', views.literature, name='literature'),
    url(r'^film/$', views.film, name='film'),
    url(r'^television/$', views.television, name='television'),
    url(r'^boardgame/$', views.boardgame, name='boardgame'),
    url(r'^videogame/$', views.videogame, name='videogame'),
    url(r'^music/$', views.music, name='music'),
    url(r'^podcast/$', views.podcast, name='podcast'),
    url(r'^beer/$', views.beer, name='beer'),
    url(r'^wine/$', views.wine, name='wine'),
    url(r'^cheese/$', views.cheese, name='cheese'),

    url(r'^fooditems/$', views.foodItem, name='fooditems'),
    url(r'^recipes/$', views.recipe, name='recipes'),
    url(r'^cooking/$', views.cooking, name='cooking'),
    url(r'^grocerypurchase/$', views.grocerypurchase, name='grocerypurchase'),
    url(r'^meal/$', views.meal, name='meal'),

    url(r'^travel/$', views.travel, name='travel'),
    url(r'^filmwish/$', views.filmwish, name='filmwish'),
]