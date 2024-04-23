from django.urls import path
from . import views

app_name='dashboard'
urlpatterns = [
    path('open-dashboard/', views.open_dashboard, name='open_dashborad'),
]