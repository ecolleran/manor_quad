from django.shortcuts import render
import random
from .wordle import Guess, Solution

# Create your views here.

wordOfDay = ''
lang_files = {'gameplay/languages/en.txt': 'English',
              'gameplay/languages/de.txt': 'German',
              'gameplay/languages/es.txt': 'Spanish',
              'gameplay/languages/fr.txt': 'French',
              'gameplay/languages/pt.txt': 'Portuguese'
}
wordSet = {}
solution = ''
num_guesses = 0
guess_left = 6
found_word = False
yellow = ''
gray = ''
green = ''
firstLet = ''
firstguess = 'XXXXX'
secondguess = 'XXXXX'
thirdguess = 'XXXXX'
fourthguess = 'XXXXX'
fifthguess = 'XXXXX'
lastguess = 'XXXXX'

def desired_lang(request):
    if request.method == 'GET':
        return render(request, 'gameplay/choose_lang.html')
    else:
        print(request.POST)

def start_game(request, lang_file = 'gameplay/languages/en.txt'):
    global wordOfDay
    global wordSet
    global solution
    global num_guesses
    global found_word
    global guess_left
    global green, gray, yellow
    global firstguess, secondguess, thirdguess, fourthguess, fifthguess, lastguess

    if request.method == 'GET':
        num_guesses = 0
        wordSet = readWordSet(lang_file)
        wordOfDay = random.choice(list(wordSet))
        solution = Solution(wordOfDay, len(wordOfDay))
        print(wordOfDay, solution)
    elif num_guesses < 6 and request.method == 'POST' and not found_word:
        if request.POST['curr_guess'].upper() not in wordSet or len(request.POST['curr_guess']) != 5:
            print('Invalid word!', request.POST['curr_guess'])
            return render(request, 'gameplay/config_game.html', {
                'guesses_left': guess_left,
                'language_selected': 'English',
                'word_of_day': wordOfDay,
                'solution': solution,
                'yellow_letters': yellow,
                'gray_letters': gray,
                'green_letters': green,
                'firstguess': firstguess,
                'secondguess': secondguess,
                'thirdguess': thirdguess,
                'fourthguess': fourthguess,
                'fifthguess': fifthguess,
                'lastguess': lastguess,
            })

        num_guesses += 1
        
        print(request.POST)
        print('num_guesses', num_guesses)
        guessedString = request.POST['curr_guess']

        guess = Guess(guessedString, len(guessedString))
        if num_guesses == 1:
            firstguess = guess.string
        elif num_guesses == 2:
            secondguess = guess.string
        elif num_guesses == 3:
            thirdguess = guess.string
        elif num_guesses == 4:
            fourthguess = guess.string
        elif num_guesses == 5:
            fifthguess = guess.string
        elif num_guesses == 6:
            lastguess = guess.string

        guess_left -= 1
        yellow, gray, green = solution.evaluateLetters(guess.string)
        found_word = all(green)
        if found_word:
            print('WORD FOUND!')
            guess_left = f'Well done! You won in {num_guesses} guesses.'

    elif num_guesses == 6:
        guess_left = 'NO GUESSES LEFT!'
    
    elif found_word:
        print('WORD FOUND!')
        guess_left = f'Well done! You won in {num_guesses} guesses.'
    


    # Render the config_game.html template with necessary context
    return render(request, 'gameplay/config_game.html', {
        'guesses_left': guess_left,
        'language_selected': lang_files[lang_file],
        'word_of_day': wordOfDay,
        'solution': solution,
        'yellow_letters': yellow,
        'gray_letters': gray,
        'green_letters': green,
        'firstguess': firstguess,
        'secondguess': secondguess,
        'thirdguess': thirdguess,
        'fourthguess': fourthguess,
        'fifthguess': fifthguess,
        'lastguess': lastguess,
    })

def start_game_GERMAN(request):
    return start_game(request, 'gameplay/languages/de.txt')

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
