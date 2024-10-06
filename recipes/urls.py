from django.urls import path

from recipes.views import (recipes, recipe_single, add_to_fav, remove_from_fav, 
                           RecipelistView, RecipeDetailView)

urlpatterns = [
    # path("", recipes, name="recipes"),
    path("", RecipelistView.as_view(), name="recipes"),
    
    # path("<slug:slug>/", recipe_single, name="recipe_single"),
    path("<slug:slug>/", RecipeDetailView.as_view(), name="recipe_single"),

    path("add-to-fav/<int:id>/", add_to_fav, name="add_to_fav"),
    path("remove-from-fav/<int:id>/", remove_from_fav, name="remove_from_fav"),
    
]