from bs4 import BeautifulSoup
import requests
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def db_connect():
    try:
        db = psycopg2.connect(
            host = "localhost", 
            dbname = "Ingredients", 
            user = "postgres", 
            password = "123", 
            port = 5432  
        )
        return db
    except psycopg2.Error as e:
        print("Database connection error", e)
        return None
    
def create_db():
    connected = db_connect()
    if connected:
        cur = connected.cursor()

    # create ingredients db
    create_ingredients_table = """
        CREATE TABLE IF NOT EXISTS ingredients (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """
    cur.execute(create_ingredients_table)

    # parse for ingredient data using beautifulSoup 
    ingredientsurl = 'https://zelda-archive.fandom.com/wiki/Category:Cooking_Ingredients'
    ingredients = requests.get(ingredientsurl)
    full_page = BeautifulSoup(ingredients.text, 'html')
    ingredient_links = full_page.find_all('a', class_ = 'category-page__member-link')

    ingredient_array = []
    for link in ingredient_links:
        ingredient_array.append(link.text)

    for ingredient in ingredient_array:
        cur.execute("INSERT INTO Ingredients (name) VALUES (%s)", (ingredient,))

    # create recipes db
    create_recipes_table = """
        CREATE TABLE IF NOT EXISTS recipes (
            id SERIAL PRIMARY KEY,
            recipe VARCHAR(255) NOT NULL,
            ingredient_1 VARCHAR(255) NOT NULL,
            ingredient_2 VARCHAR(255),
            ingredient_3 VARCHAR(255),
            ingredient_4 VARCHAR(255),
            ingredient_5 VARCHAR(255)
        )
    """
    cur.execute(create_recipes_table)

    # parse for recipe data using beautifulSoup
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

    for recipe in recipes_array:
        name = recipe[0]
        ingr = recipe[1][:5]
        while len(ingr) < 5:
            ingr.append(None)

        cur.execute("""
            INSERT INTO recipes (recipe, ingredient_1, ingredient_2, ingredient_3, ingredient_4, ingredient_5)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, ingr[0], ingr[1], ingr[2], ingr[3], ingr[4]))

    connected.commit()
    cur.close()
    connected.close()

# execute initialization
create_db()