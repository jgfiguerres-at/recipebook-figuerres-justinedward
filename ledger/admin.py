from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Ingredient, Recipe, RecipeIngredient


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInLine,
    ]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)
    list_filter = ()
    search_fields = ('name',)

    fieldsets = [
        ('Details', {
            'fields': [
                'name',
            ]
        })
    ]


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name', 'author', 'created_on', 'updated_on',)
    list_filter = ('author',)
    search_fields = ('name',)
    
    fieldsets = [
        ('Details', {
            'fields': [
                'name',
                'author',
            ]
        })
    ]
    
    inlines = [
        RecipeIngredientInline,
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
