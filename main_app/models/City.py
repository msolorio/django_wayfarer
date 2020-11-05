from django.db import models
from django.contrib.auth.models import User

def getFullName(self):
    return f'{self.name}, {self.country}'

class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    population = models.IntegerField(default=0)
    photo_url = models.CharField(
        max_length=500,
        default='',
        blank=True
    )

    def getFullName(self):
        return getFullName(self)

    def __str__(self):
        return getFullName(self)
