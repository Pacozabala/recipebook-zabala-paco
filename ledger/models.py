from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name = 'recipe'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name = 'ingredients'
    )
    
    def __str__(self):
        return f"{self.recipe}: {self.quantity} of {self.ingredient}"
        
    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])
