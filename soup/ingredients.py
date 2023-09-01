# parsing for BOTW ingredients
from bs4 import BeautifulSoup
import requests

ingredientsurl = 'https://zelda-archive.fandom.com/wiki/Category:Cooking_Ingredients'
ingredients = requests.get(ingredientsurl)
full_page = BeautifulSoup(ingredients.text, 'html')
ingredient_links = full_page.find_all('a', class_ = 'category-page__member-link')

for link in ingredient_links:
    print(link.text)