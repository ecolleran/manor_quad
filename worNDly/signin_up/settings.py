from django.urls import path

from . import views
app_name = ‘signin_up’  # creates a namespace for this app
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.view_post, name='view_post'),

]
