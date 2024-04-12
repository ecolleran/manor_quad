from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Player

# Create your views here.

''' Feature 1.1: Create User '''
def create_new_user(request):
    if request.method == 'GET':
        return render(request, 'signin_up/sign_in.html')
    else:
        print(request.POST)
        for p in Player.objects.all():
            if p.username == request.POST['username']:
                print('User already taken')
                return render(request, 'signin_up/sign_in.html')
        

        player = Player.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        return redirect('/', {'new_user': '', 'new_name': '', })

'''class CreateNewPlayer(View):
    def get(request):
        return render(request, 'user/login.html', {'form': UserForm(), 'user': request.user.is_authenticated})'''

    

''' Feature 1.2: Sign-in '''
def login_users(request):
    if request.method == 'GET':
        return render(request, "signin_up/login_user.html")
    else:
        print(request.POST)
        for p in Player.objects.all():
            if p.username == request.POST['username'] and p.password == request.POST['password']:
                logged_in = Player(username = request.POST['username'], password = request.POST['password'])
                new_user = True
                new_name = logged_in.username
                print(new_user, new_name)
                return render(request, 'homepage.html', {'new_user': new_user, 'new_name': new_name})
        
        return render(request, "signin_up/login_user.html")

#class LoginView(View):
    #pass

''' Feature 1.3: Sign-out '''
'''def site_logout(request):
    logout(request)
    return HttpResponseRedirect('/')'''

#class LogoutView(View):
    #pass

