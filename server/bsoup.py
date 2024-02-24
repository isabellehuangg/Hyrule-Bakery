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
    all_recipes = [] 
    for name, ingredients in zip(recipe_divs, ingredients_divs):
        one_recipe = []
        one_recipe.append(name.text.strip())

        cleaned_ingredients = ingredients.text.strip().split('\n')
        cleaned_ingredients_2 = []

        for i, ingredient in enumerate(cleaned_ingredients):
            if ingredient.strip():
                cleaned_ingredients_2[i] = ingredient.strip()
        one_recipe.append(cleaned_ingredients_2)

        all_recipes.append(one_recipe)

    all_with_or = []
    for recipe in all_recipes:
        if "or" in any(ingr for ingr in recipe[1]):
            end = recipe[1][3:]
            options = [recipe[0], recipe[2]]
            for option in options:
                tmp = [option] + end
                all_with_or.append([recipe[0], tmp])
        else:
            all_with_or.append(recipe)
    
    return all_with_or
