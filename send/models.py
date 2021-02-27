from django.db import models

# Create your models here.
class Whatsapp_Numbers(models.Model):
    number=models.IntegerField()

    def __str__(self):
        return str(self.number)