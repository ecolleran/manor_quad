from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Wallet(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.player.username