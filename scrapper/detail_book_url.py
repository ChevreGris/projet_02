import requests
from bs4 import BeautifulSoup


def get_all_categories_pages(url_categories):
    #fonction qui trouve la ou les urls d'une categorie.

    response = requests.get (url_categories)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        category_pages_url = []

        try:
            pages = soup.find(class_='current').text
            last_pages_nbrs_int = int(pages.replace('Page 1 of ' , ''))
            
        except AttributeError:
            category_pages_url.append(url_categories)
            return category_pages_url
        else:
            category_pages_url.append(url_categories)
            for page_nbr in range(2, last_pages_nbrs_int + 1):
                category_pages_url.append(url_categories.replace('index' , 'page-' + str(page_nbr)))
            return category_pages_url


#fonction qui trouve toutes les urls des livres dans une page d'une categorie.
def get_book_url(url_categories):
    response = requests.get (url_categories)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        books_urls = []

        for url in soup.select("h3 a"):
            books_urls.append('http://books.toscrape.com/catalogue/' + url["href"].replace('../../../',''))
        
        return books_urls


def get_all_books_links(url_categories):
    #fonction qui trouve toutes les urls des livres dans toutes les pages d'une categorie.

    all_books_links = []

    io = get_all_categories_pages(url_categories)

    for links in io:
        all_books_links.extend(get_book_url(links))
    return all_books_links


