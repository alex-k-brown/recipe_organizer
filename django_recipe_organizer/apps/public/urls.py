from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf import settings

urlpatterns = patterns(
    'apps.public.views',

    url(r'^recipes/$', RecipeList.as_view(), name='recipe-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^ingredients/$', IngredientList.as_view(), name='ingredient-list'),

    url(r'^add-recipe/$', AddRecipe.as_view(), name='recipe-list'),
)