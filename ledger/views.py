from django.shortcuts import render
from django.http import HttpResponse

def recipe_list(request):
    ctx = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {
                        "name": "tomato",
                        "quantity": "3 pcs"
                    },
                    {
                        "name": "onion",
                        "quantity": "1 pc"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kg"
                    },
                    {
                        "name": "water",
                        "quantity": "1 L"
                    },
                    {
                        "name": "sinigang mix",
                        "quantity": "1 packet"
                    }
                ],
                "link": "/recipe/1"
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {
                        "name": "garlic",
                        "quantity": "1 head"
                    },
                    {
                        "name": "onion",
                        "quantity": "1 pc"
                    },
                    {
                        "name": "vinegar",
                        "quantity": "1/2 cup"
                    },
                    {
                        "name": "water",
                        "quanity": "1 cup"
                    },
                    {
                        "name": "salt",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "whole black peppers",
                        "quantity": "1 tablespoon"
                    },
                    {
                        "name": "pork",
                        "quantity": "1 kilo"
                    }
                ],
                "link": "/recipe/2"
            }
        ]
    }

    return render(request, "recipebook/recipe_list.html", ctx)

def recipe(request, number):
    if (number == 1):
        ctx = {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3 pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1 pc"
                },
                {
                    "name": "pork",
                    "quantity": "1 kg"
                },
                {
                    "name": "water",
                    "quantity": "1 L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        }
    elif (number == 2):
        ctx = {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1 pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2 cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }

    return render(request, "recipebook/recipe.html", ctx)