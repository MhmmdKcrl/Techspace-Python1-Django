from rest_framework import serializers

from recipes.models import Category, Tags, Recipe



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'id','name', 'created_at', 'updated_at']




class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ['id', 'name', 'created_at',]





class CategoryRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [ 'id','name']




class RecipeSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.name')
    category = CategoryRecipeSerializer()
    tags = TagSerializer(many = True)
    # author = serializers.CharField(source='author.username')

    class Meta:
        model = Recipe
        fields = [
                    'id', 
                  'title', 
                  'description', 
                  'image', 
                  'category', 
                  'tags', 
                #   'author',
                  'author_fullname'
                  ]
        

class RecipeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
                 'id', 
                  'title', 
                  'description', 
                  'image', 
                  'category', 
                  'tags', 
                  'author',
                  ]