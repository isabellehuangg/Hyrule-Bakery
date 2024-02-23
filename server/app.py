from flask import Flask
from db import db_connect

app = Flask(__name__)

# all things API
# URL: http://127.0.0.1:5000/api/ingredients
# @app.route('/', methods=['GET'])
# def hello():
#     return("Hello world")

@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    connected = db_connect()
    if connected:
        cur = connected.cursor()
        cur.execute("""SELECT name FROM ingredients""")
        all_ingr = [row[0] for row in cur.fetchall()]

        cur.close()
        connected.close()
        return all_ingr

@app.route('/recipe', methods=["GET"])
def recipes_names():
    connected = db_connect()
    if connected:
        cur = connected.cursor()
        cur.execute("""SELECT recipe, ingredient_1, ingredient_2, ingredient_3, ingredient_4, ingredient_5 FROM recipes""")
        data = cur.fetchall()
        cur.close()
        connected.close()
        return data

if __name__ == '__main__':
    app.run()
    