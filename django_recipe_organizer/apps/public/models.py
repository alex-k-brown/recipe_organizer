from django.db import models
from decimal import Decimal

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient')
    categories = models.CharField(max_length=50)
    description = models.TextField()
    instructions = models.ManyToManyField('Instruction')
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    time = models.FloatField(default=0)

    def __unicode__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=100, default=0)

    def __unicode__(self):
        return self.name

class Instruction(models.Model):
    name = models.CharField(max_length=100)
    instruction = models.TextField()
    video = models.URLField()

    def __unicode__(self):
        return self.name

class Takeout(models.Model):
    name = models.CharField(max_length=100)
    restaurants = models.URLField()
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    rating = models.DecimalField(decimal_places=1, max_digits=3)

    def __unicode__(self):
        return self.name
