from models import *
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        depth = 1


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


class TakeoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takeout