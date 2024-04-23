from django.urls import path
from . import views

app_name='gameplay'
urlpatterns = [
    path('start-game/', views.start_game, name='start_game'),
]
