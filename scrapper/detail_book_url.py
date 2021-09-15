import requests
from bs4 import BeautifulSoup

def get_book_url(url_categories):
    response = requests.get (url_categories)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        books_urls = []

        for url in soup.select("ol a"):
            books_urls.append('http://books.toscrape.com/catalogue/' + url["href"].replace('../../../',''))
        
        return books_urls
