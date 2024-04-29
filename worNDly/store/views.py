from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from signin_up.models import Player  # Import Player model from signin_up app
from .models import Wallet

# Create your views here.

def open_store(request):
    return render(request, 'homepage.html', {'new_user': False, 'new_name': ''})

def purchase_games(request):
    player = Player.objects.get(email=request.user.email)
    wallet_user = Wallet.objects.get(player=player)

    if request.method == 'POST':
        num_games = int(request.POST.get('num_games', 0))
        if num_games <= 0:
            messages.error(request, 'Please enter a valid number of games.')
            return redirect('purchase_games')

        # Logic to deduct coins and make API request goes here
        # Replace this with your actual logic

        messages.success(request, f'Successfully purchased {num_games} games.')
        return redirect('purchase_games')

    return render(request, 'store/purchase_games.html', {'user_profile': wallet})
