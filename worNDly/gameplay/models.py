from django.db import models



# Create your models here.

'''class Game_In_Play(models.Model):
    GERMAN = "de.txt"
    SPANISH = "es.txt"
    FRENCH = "fr.txt"
    PORTUGUESE = "pt.txt"
    ENGLISH = "en.txt"
    LANGS = {
        GERMAN: "German",
        SPANISH: "Spanish",
        FRENCH: "French",
        PORTUGUESE: "Portuguese",
        ENGLISH: "English",
    }
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateTimeField('date played')
    language = models.CharField(
        choices=LANGS,
        default=ENGLISH,
    )
    correct_word = models.CharField(max_length=50)
    good_letters = ArrayField(
        models.CharField(max_length=1),
        size=5,
    )
    good_letters = ArrayField(
        models.CharField(max_length=1),
        size=21,
    )
    good_letters = ArrayField(
        models.CharField(max_length=1),
        size=5,
    )
    fail = models.BooleanField()
    attempts = models.IntegerField(max_length=6)'''