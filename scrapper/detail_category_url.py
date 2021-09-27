import requests
from bs4 import BeautifulSoup


def get_category_urls_and_names(main_url):
    # fonction qui trouve les urls de chaque categories et leur nom.

    response = requests.get(main_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        categories = []

        for category in soup.select(".nav.nav-list ul a"):
            categories.append(['http://books.toscrape.com/' + category["href"],
                              category.text.strip()])

        return categories
