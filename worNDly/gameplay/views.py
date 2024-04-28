from django.shortcuts import render

# Create your views here.

def desired_lang(request):
    if request.method == 'GET':
        return render(request, 'gameplay/choose_lang.html')
    else:
        print(request.POST)

def start_game(request):
    file = 'gameplay/languages/en.txt'
    language = request.POST.get('language')
    
    if language == 'GERMAN':
        file='gameplay/languages/de.txt'
    elif language == 'SPANISH':
        file += 'gameplay/languages/es.txt'
    elif language == 'PORTUGUESE':
        file += 'gameplay/languages/pt.txt'
    elif language == 'FRENCH':
        file += 'gameplay/languages/fr.txt'

    # Make sure to handle file not found or other errors here
    wordSet = {word.strip() for word in open(file)}

    return render(request, 'gameplay/config_game.html')
