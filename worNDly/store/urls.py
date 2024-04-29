from django.urls import path
from . import views

app_name='store'
urlpatterns = [
    path('purchase_games/', views.purchase_games, name='purchase_games'),
]