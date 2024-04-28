from django.urls import path
from . import views

app_name='gameplay'
urlpatterns = [
    path('start_game/', views.start_game, name='start_game'),
    path('start_game/GERMAN', views.start_game_GERMAN, name='start_game_GERMAN'),
    path('start_game/SPANISH', views.start_game_SPANISH, name='start_game_SPANISH'),
    path('start_game/PORT', views.start_game_PORT, name='start_game_PORT'),
    path('start_game/FRENCH', views.start_game_FRENCH, name='start_game_FRENCH'),
    path('desired_lang/', views.desired_lang, name='desired_lang')
]
