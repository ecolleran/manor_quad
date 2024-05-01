# views.py

from django.shortcuts import render
from django import forms
from django.contrib.auth.decorators import login_required
import requests

class BuyGamePlaysForm(forms.Form):
    num_plays = forms.IntegerField(label='Number of game plays to purchase (number > 1)')

    
def view_balance(access_token, email):
   # Use the access token to make an authenticated request
   headers = {'Authorization': f'Bearer {access_token}'}
   # Make a GET request with the authorization header
   api_response = requests.get(f"https://jcssantos.pythonanywhere.com/api/group10/group10/player/{email}/", headers=headers)
   if api_response.status_code == 200:
       # Process the data from the API
       return api_response.json()['amount']
   else:
       print("Failed to access the API endpoint to view balance for user:", api_response.status_code)

def buy_game_plays(access_token, email, num_plays):
    current_balance = view_balance(access_token, email)
    print(current_balance)
    cost = num_plays
    if current_balance >= cost:
        url = f"https://jcssantos.pythonanywhere.com/api/group10/group10/player/{email}/pay"
        data = {"amount": cost}
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            new_balance = response.json()["new_amount"]
            return f"Successfully purchased {num_plays} extra game plays. New coin balance: {new_balance}"
        else:
            return response.json()["message"]  # Error message from API
    else:
        return "Insufficient funds to purchase game plays"

@login_required
def purchase_games(request):
    if request.method == 'POST':
        form = BuyGamePlaysForm(request.POST)
        if form.is_valid():
            email = request.user.email
            num_plays = form.cleaned_data['num_plays']
            access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIzMjQ0MTU1LCJpYXQiOjE3MTQ2MDQxNTUsImp0aSI6IjJiYmE5YzIyNjg3OTQzNjRiNjQxOGIxMTQ3MWYzZGRlIiwidXNlcl9pZCI6ODV9.u923TBU1kxjBtstv-5Dt8RptBIaxTIC3UP4p5Du8m5k"
            response = buy_game_plays(access_token, email, num_plays)
            return render(request, 'store/purchase_games.html', {'form': form, 'response': response}) # Pass the form back to the template
    else:
        form = BuyGamePlaysForm()
    return render(request, 'store/purchase_games.html', {'form': form})


