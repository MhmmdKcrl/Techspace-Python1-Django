from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import Category, Recipe, Favourites

class RecipelistView(ListView):
    template_name = 'recipes.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


def recipes(request):
    recipes = Recipe.objects.all()  # select * from recipes_recipe
    # Recipe.objects.raw("select * from recipes_recipe")
    # categories = Category.objects.all()

    if request.user.is_authenticated:
        user = request.user
        user_favs = [i.recipe for i in user.favourites.all()]
        for i in recipes:
            if i in user_favs:
                i.is_fav = True
            else:
                i.is_fav = False
    else:
        sessions = request.session.get('favs', [])
        # sessions = request.COOKIES.get('favs', [])
        if sessions:
            print(sessions, "+++++++++++++")
            for i in recipes:
                if i.id in sessions:
                    i.is_fav = True
                else:
                    i.is_fav = False

    context = {
        "recipes": recipes,
        # "categories": categories
    }
    return render(request, "recipes.html", context)


class RecipeDetailView(DetailView):
    template_name = 'single.html'
    model = Recipe
    context_object_name = 'recipe'


def recipe_single(request, slug):
    # recipe = Recipe.objects.get(id=recipe_id)
    recipe = Recipe.objects.get(slug=slug)

    context = {
        "recipe": recipe
    }

    return render(request, "single.html", context)



def add_to_fav(request, id):
    recipe = Recipe.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        if Favourites.objects.filter(user=user, recipe=recipe).first() == None:
            Favourites.objects.create(user=user, recipe=recipe)
            messages.add_message(request, messages.SUCCESS, "Recipe added to favourites")
        else:
            messages.add_message(request, messages.INFO, "Recipe already in favourites")

       
    else:
        if recipe:
            sessions = request.session.get('favs', [])
            # sessions = request.COOKIES.get('favs', [])
            
            print(sessions, "--------------")
            if not (recipe.id in sessions):
                request.session['favs'] = sessions
                # request.COOKIES['favs'] = sessions
                
                sessions.append(recipe.id)
                messages.add_message(request, messages.SUCCESS, "Recipe added to favourites")
            else:
                messages.add_message(request, messages.INFO, "Recipe already in favourites")

    
    return redirect('recipes')



def remove_from_fav(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.user.is_authenticated:
        user = request.user
        fav = Favourites.objects.filter(user=user, recipe=recipe).first()
        if fav:
            fav.delete()
            messages.add_message(request, messages.SUCCESS, "Recipe removed from favourites")
        else:
            messages.add_message(request, messages.ERROR, "Recipe not in favourites")

    else:
        sessions = request.session.get('favs', [])
        if recipe:
            if recipe.id in sessions:
                sessions.remove(recipe.id)
                request.session['favs'] = sessions
                messages.add_message(request, messages.SUCCESS, "Recipe removed from favourites")
            else:
                messages.add_message(request, messages.INFO, "Recipe not in favourites")


    return redirect('recipes')
