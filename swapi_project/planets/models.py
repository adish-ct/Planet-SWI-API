from django.db import models

# Create your models here.

# using external api to write entry on the table so allowing null and blank.
class Planet(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    population = models.CharField(max_length=50, null=True, blank=True)
    climates = models.CharField(max_length=200, null=True, blank=True)
    terrains = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name