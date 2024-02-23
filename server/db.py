import psycopg2
import os
from bsoup import scrape_ingredients, scrape_recipes
from sql import create_recipes_table, create_ingredients_table

def db_connect():
    try:
        db = psycopg2.connect(
            host = "localhost", 
            dbname = "Ingredients", 
            user = "postgres", 
            password = os.environ.get('DB_PW'), 
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

    cur.execute(create_ingredients_table)
    cur.execute(create_recipes_table)

    ingredient_array = scrape_ingredients()
    recipes_array = scrape_recipes()

    for ingredient in ingredient_array:
        cur.execute("INSERT INTO Ingredients (name) VALUES (%s)", (ingredient,))

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

create_db()
