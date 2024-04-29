from django.shortcuts import render
import random
from .wordle import Guess, Solution

# Create your views here.

def desired_lang(request):
    if request.method == 'GET':
        return render(request, 'gameplay/choose_lang.html')
    else:
        print(request.POST)

def start_game(request):
    language = request.POST.get('language')
    wordSet = readWordSet(language)
    wordOfDay = random.choice(list(wordSet))
    solution = Solution(wordOfDay, len(wordOfDay))
    
    # Render the config_game.html template with necessary context
    return render(request, 'gameplay/config_game.html', {
        'language_selected': language,
        'word_of_day': wordOfDay,
        'solution': solution,
    })

def readWordSet(language):
    # Define file paths based on selected language
    language_files={
        'GERMAN': 'gameplay/languages/de.txt',
        'ENGLISH': 'gameplay/languages/en.txt',
        'SPANISH': 'gameplay/languages/es.txt',
        'PORTUGUESE': 'gameplay/languages/pt.txt',
        'FRENCH': 'gameplay/languages/fr.txt',
    }

    file=language_files.get(language, "gameplay/languages/en.txt")
    return {word.strip() for word in open(file)}
