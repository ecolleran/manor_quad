from django.shortcuts import render
from django.contrib.auth.models import User
from gameplay.models import GamesPlayed
import datetime

# Create your views here.

def open_dashboard(request):
    listOfPlays = []
    listOfPlaysYEAR = []
    listOfPlaysMONTH = []
    listOfPlaysWEEK = []


    for g in GamesPlayed.objects.all():
        if request.user == g.player:
            print(g)
            listOfPlays.append(g)
        
        if request.user == g.player and g.game_play_date.year == datetime.datetime.now().year:
            print(g)
            listOfPlaysYEAR.append(g)
        
        if request.user == g.player and g.game_play_date.month == datetime.datetime.now().month:
            print(g)
            listOfPlaysMONTH.append(g)
        
        if request.user == g.player and g.game_play_date.isocalendar()[1] == datetime.datetime.now().isocalendar()[1]:
            print(g)
            listOfPlaysWEEK.append(g)
        
        
        
        
        

        


    return render(request, 'dashboard/firstdash.html', {'listOfPlays': listOfPlays, 'listOfPlaysYEAR': listOfPlaysYEAR, 'listOfPlaysMONTH': listOfPlaysMONTH, 'listOfPlaysWEEK': listOfPlaysWEEK})