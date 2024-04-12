from django.urls import path
from . import views


# URL Patterns

urlpatterns = [
    path('create/', views.create_new_user, name="create")
]

#path('sign_in/', CreateUserView.as_view()),
#path('sign_out/', LogoutView.as_view()),