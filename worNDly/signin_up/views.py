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
        return redirect('/')

class CreateNewPlayer(View):
    def get(request):
        return render(request, 'user/login.html', {'form': UserForm(), 'user': request.user.is_authenticated})

    

''' Feature 1.2: Sign-in '''
#def site_login(request):
    #pass

#class LoginView(View):
    #pass

''' Feature 1.3: Sign-out '''
'''def site_logout(request):
    logout(request)
    return HttpResponseRedirect('/')'''

#class LogoutView(View):
    #pass

