from modeltranslation.translator import translator, TranslationOptions
from recipes.models import Tags, Category, Recipe


class TagsTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class RecipeTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(Tags, TagsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Recipe, RecipeTranslationOptions)