from django.db import models

# Create your models here.

class Wallet(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    purchase_amount = models.IntegerField()
    success= models.BooleanField()