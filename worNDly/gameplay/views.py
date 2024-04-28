from django.shortcuts import render


# Create your views here.

def desired_lang(request):
    if request.method == 'GET':
        return render(request, 'gameplay/choose_lang.html')
    else:
        print(request.POST)
        

def start_game(request):
    wordSet = {word.strip() for word in open('gameplay/languages/en.txt')}

    return render(request, 'gameplay/config_game.html', {'language_selected': 'English'})

def start_game_GERMAN(request):
    wordSet = {word.strip() for word in open('gameplay/languages/de.txt')}
    return render(request, 'gameplay/config_game.html', {'language_selected': 'German'})

def start_game_SPANISH(request):
    wordSet = {word.strip() for word in open('gameplay/languages/es.txt')}
    return render(request, 'gameplay/config_game.html', {'language_selected': 'Spanish'})

def start_game_PORT(request):
    wordSet = {word.strip() for word in open('gameplay/languages/pt.txt')}
    return render(request, 'gameplay/config_game.html', {'language_selected': 'Portuguese'})

def start_game_FRENCH(request):
    wordSet = {word.strip() for word in open('gameplay/languages/fr.txt')}
    return render(request, 'gameplay/config_game.html', {'language_selected': 'French'})