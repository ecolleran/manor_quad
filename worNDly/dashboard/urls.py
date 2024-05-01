from django.urls import path
from . import views

app_name='dashboard'
urlpatterns = [
    path('open_dashboard/', views.open_dashboard, name='open_dashboard'),
    path('show_statistics/', views.show_statistics, name='show_statistics')
]