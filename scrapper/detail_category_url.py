import requests
from bs4 import BeautifulSoup

"""
#fonction qui trouve les urls de chaque categories.
def get_category_urls(main_url):
    response = requests.get (main_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        categories = []

        for category in soup.select(".nav.nav-list ul a"):
            categories.append('http://books.toscrape.com/' + category["href"])
            categories.append(category.text.strip())
        return categories
        
"""

#"""
#fonction qui trouve les urls de chaque categories.
def get_category_urls(main_url):
    response = requests.get (main_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        categories = []

        for category in soup.select(".nav.nav-list ul a"):
            categories.append('http://books.toscrape.com/' + category["href"])
        return categories
        
#"""

#"""
#fonction qui trouve les noms de chaque categories.
def get_category_names(main_url):
    response = requests.get (main_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        categories_names = []

        for category in soup.select(".nav.nav-list ul a"):
            categories_names.append(category.text.strip())
        return categories_names
#"""