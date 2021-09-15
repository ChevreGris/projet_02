import requests
from bs4 import BeautifulSoup

def get_category_urls(main_url):
    response = requests.get (main_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        categories = []

        for category in soup.select(".nav.nav-list ul a"):
            categories.append('http://books.toscrape.com/' + category["href"])

        return categories



   