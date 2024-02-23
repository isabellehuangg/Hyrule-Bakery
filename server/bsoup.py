from bs4 import BeautifulSoup
import requests

def scrape_ingredients():
    ingredientsurl = 'https://zelda-archive.fandom.com/wiki/Category:Cooking_Ingredients'
    ingredients = requests.get(ingredientsurl)
    full_page = BeautifulSoup(ingredients.text, 'html')
    ingredient_links = full_page.find_all('a', class_ = 'category-page__member-link')

    ingredient_array = []
    for link in ingredient_links:
        ingredient_array.append(link.text)
    return ingredient_array

def scrape_recipes():
    recipesurl = 'https://rankedboost.com/zelda-tears-of-the-kingdom/dessert-recipe/'
    recipes = requests.get(recipesurl)
    full_page2 = BeautifulSoup(recipes.text, 'html')
    recipe_divs = full_page2.find_all('div', 'rbss-object-name-pokedex-css-div')
    ingredients_divs = full_page2.find_all('div', 'rbss-class-skill-desc-data-holder rbss-ztotk')

    # lists in list containing ingredient + recipe 
    recipes_array = [] 
    singular_recipe_array = []
    for recipe_name, list_ingredients in zip(recipe_divs, ingredients_divs):
        singular_recipe_array.append(recipe_name.text.strip())
        singular_ingredients = list_ingredients.text.strip().split('\n')
        singular_ingredients_2 = [ingredient.strip() for ingredient in singular_ingredients if ingredient.strip()]
        singular_recipe_array.append(singular_ingredients_2)
        recipes_array.append(singular_recipe_array)
        singular_recipe_array = []
    
    return recipes_array