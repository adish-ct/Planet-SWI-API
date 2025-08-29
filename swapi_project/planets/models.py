from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=50)
    climates = models.CharField(max_length=200)
    terrains = models.CharField(max_length=200)

    def __str__(self):
        return self.name