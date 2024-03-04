from django.contrib import admin

from .models import Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    
    search_fields = ('ingredient', )
    list_display = ('recipe', 'ingredient', 'quantity', )
    list_filter = ('recipe', 'ingredient', )

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline,]
    
admin.site.register(Recipe)
