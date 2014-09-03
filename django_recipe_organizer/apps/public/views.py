from django.shortcuts import render
from models import *
from serializers import *
from rest_framework import generics

# Create your views here.

class RecipeList(generics.ListAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class IngredientList(generics.ListCreateAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class PreparationList(generics.ListAPIView):
    model = Instruction
    serializer_class = PreparationSerializer
    queryset = Instruction.objects.all()


class TakeoutList(generics.ListAPIView):
    model = Takeout
    serializer_class = TakeoutSerializer
    queryset = Takeout.objects.all()