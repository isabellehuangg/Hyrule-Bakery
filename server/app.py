# parsing for BOTW ingredients
from bs4 import BeautifulSoup
import requests
import psycopg2
from flask import Flask, jsonify

#initialize Flask application
app = Flask(__name__)

# parse for ingredient data using beautifulSoup 
ingredientsurl = 'https://zelda-archive.fandom.com/wiki/Category:Cooking_Ingredients'
ingredients = requests.get(ingredientsurl)
full_page = BeautifulSoup(ingredients.text, 'html')
ingredient_links = full_page.find_all('a', class_ = 'category-page__member-link')

ingredient_array = []
for link in ingredient_links:
    ingredient_array.append(link.text)

# parse for recipe data using beautifulSoup
recipesurl = 'https://www.ign.com/wikis/the-legend-of-zelda-breath-of-the-wild/All_Recipes_and_Cookbook'
recipes = requests.get(recipesurl)
full_page2 = BeautifulSoup(recipes.text, 'html')
recipe_links = full_page2.find_all()

recipe_array = [] # result of ingr. combo

# connect to PostgreSQL database
db = psycopg2.connect(
    host = "localhost", 
    dbname = "Ingredients", 
    user = "postgres", 
    password = "123", 
    port = 5432
)
cur = db.cursor()

# create ingredients table
create_ingredients_table = """
    CREATE TABLE IF NOT EXISTS ingredients (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
"""
cur.execute(create_ingredients_table)

for ingredient in ingredient_array:
    cur.execute("INSERT INTO Ingredients (name) VALUES (%s)", (ingredient,))

db.commit()
cur.close()
db.close()