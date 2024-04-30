from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from signin_up.models import Player  # Import Player model from signin_up app
# from .models import Wallet

# Create your views here.

def purchase_games(request):
    return render(request, 'homepage.html', {'new_user': False, 'new_name': ''})
