from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.name)])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', args=[str(self.name)])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_ingredient', args=[str(self.name)])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'recipe ingredient'
        verbose_name_plural = 'recipe ingredients'
