from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_users, name="login"),
    path('logout/', views.logout_users, name='logout'),
]

#path('sign_in/', CreateUserView.as_view()),
#path('sign_out/', LogoutView.as_view()),