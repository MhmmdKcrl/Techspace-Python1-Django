from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True


class Category(DateMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'  
    

class Tags(DateMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tags'
        verbose_name = 'Tag'


class Recipe(DateMixin):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='recipes')
    tags = models.ManyToManyField(Tags, related_name='recipes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = 'Recipes'
        verbose_name = 'Recipe'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse_lazy('recipe_single', kwargs={'slug': self.slug})
    
    def author_fullname(self):
        return f'{self.author.first_name} {self.author.last_name}'


class RecipeImages(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='recipes')

    def __str__(self):
        return f"{self.recipe.title} Image"
    


class Favourites(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourites')

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"
    
    class Meta:
        verbose_name_plural = 'Favourites'
        verbose_name = 'Favourite'
        ordering = ['-created_at']