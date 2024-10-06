from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

# Register your models here.

from recipes.models import Category, Tags, Recipe, RecipeImages, Favourites

admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(RecipeImages)
admin.site.register(Favourites)
# admin.site.register(Recipe)


class RecipeImagesInline(admin.TabularInline):
    model = RecipeImages
    extra = 2



@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ['id','title','slug','get_image', 'get_tags','category','author', 'created_at', 'updated_at', 'is_active']
    list_display_links = ['id','title','created_at']
    list_editable = ['category', 'author', 'is_active']
    list_filter = ['category', 'tags']
    # inlines = [RecipeImagesInline]

    fieldsets = [
        ('Recipe Info', {'fields': ['title', 'description', 'image', 'is_active', 'slug']}),
        ('Relations', {'fields': ['category', 'tags', 'author']}),
    ]



    def get_image(self, obj):
        if obj.image:
            image = f"<img src='{obj.image.url}' style='width: 50px; height: 50px;'>"
            return format_html(image)
        return 'No Image'
    get_image.short_description = 'Image'
    

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'