# find link for recipes
from bs4 import BeautifulSoup
import requests

recipesurl = 'https://www.ign.com/wikis/the-legend-of-zelda-breath-of-the-wild/All_Recipes_and_Cookbook'
recipes = requests.get(recipesurl)
BeautifulSoup(recipes.text, 'html')