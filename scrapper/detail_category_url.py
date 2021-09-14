import requests
from bs4 import BeautifulSoup

def get_category_url(main_url):
    response = requests.get (main_url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        category_url = soup.find(class_="nav nav-list")

    print(category_url)