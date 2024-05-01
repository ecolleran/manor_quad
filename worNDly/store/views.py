from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Wallet
import requests 

# Create your views here.
#just loop back to homepage while building out the app still
'''def purchase_games(request):
    return render(request, 'homepage.html', {'new_user': False, 'new_name': ''})'''

def view_all_coins(access_token):
   # Use the access token to make an authenticated request
   headers = {
       'Authorization': f'Bearer {access_token}'
   }
   # Make a GET request with the authorization header
   api_response = requests.get("https://jcssantos.pythonanywhere.com/api/group10/group10/", headers=headers)

   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()
   else:
       print("Failed to access the API endpoint to view all coins:", api_response.status_code)
    #returns a JSON file that looks like as follows: [{'player': 'jdasilv2@nd.edu', 'amount': 10}]


def view_balance_for_user(access_token, email):
   # Use the access token to make an authenticated request
   headers = {
       'Authorization': f'Bearer {access_token}'
   }
   # Make a GET request with the authorization header
   api_response = requests.get(f"https://jcssantos.pythonanywhere.com/api/group10/group10/player/{email}/", headers=headers)
   
   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()
   else:
       print("Failed to access the API endpoint to view balance for user:", api_response.status_code)
    #returns a JSON file that looks like as follows: {'amount': 10}

def user_pay(access_token, email, amount):
   # Use the access token to make an authenticated request
   headers = {
       'Authorization': f'Bearer {access_token}'
   }
   data = {"amount": amount} # non-negative integer value to be decreased
   # Make a POST request with the authorization header and data payload
   api_response = requests.post(f"https://jcssantos.pythonanywhere.com/api/group10/group10/player/{email}/pay", headers=headers, data=data)

   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()
   else:
       print("Failed to access the API endpoint to pay:", api_response.status_code)
    #returns a JSON file that looks like as follows: {'message': 'Coins decreased successfully', 'new_amount': 9}

@login_required(login_url='homepage.html')
def purchase_games(request):
    player = request.user.email
    print(player)

    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMDg5MjEzLCJpYXQiOjE3MTQ0NDkyMTMsImp0aSI6IjNjZDZjOWNhZGU2NTRiZDI4NDBjZGMzMTYzMzYyMjQxIiwidXNlcl9pZCI6MjJ9.hnjrcqGKIa6-h0Yh_oYhCp2LC0_aHlbjmqzjbF0d3MU"
    if not access_token:
        messages.error(request, 'Failed to retrieve access token. Please try again later.')
    
    user_balance = view_balance_for_user(access_token=access_token, email=player)
    print(user_balance)
    bal=request.Wallet.balance
    print(bal)
    #user_balance['amount']
    
    if request.method == 'POST':
        num_games = int(request.POST.get('num_games', 0))
        if num_games <= 0:
            messages.error(request, 'Please enter a valid number of games.')
            return redirect('purchase_games')
        
        api_response = user_pay(access_token=access_token, email=request.user.email, amount=num_games)
        if api_response and 'message' in api_response:
            if api_response['message'] == 'Coins decreased successfully':
                Wallet.balance -= num_games
                Wallet.save()
                messages.success(request, f'Successfully purchased {num_games} games.')
            else:
                messages.error(request, 'Failed to purchase games. Please try again later.')
        else:
            messages.error(request, 'Failed to purchase games. Please try again later.')

        return redirect('purchase_games')
    return render(request, 'store/purchase_games.html', {'new_balance': Wallet.balance})