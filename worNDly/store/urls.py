from django.urls import path
from . import views

app_name='store'
urlpatterns = [
    path('open_store/', views.open_store, name='opne_store'),
]