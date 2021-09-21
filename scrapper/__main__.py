from os import write
import requests
from bs4 import BeautifulSoup

from detail_book_info import get_book_info
from detail_book_url import get_all_books_links
#from detail_book_url import get_book_url
from detail_category_url import get_category_urls
from detail_category_url import get_category_names
if __name__ == '__main__':

    main_url = 'http://books.toscrape.com'
    url_categorie = 'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html'




    #'''
    def categories_data(url_de_la_categorie):
        links = get_all_books_links(url_de_la_categorie)
        data = []

        for url in links:
            data.append(get_book_info(url))
        return data
    #'''

    #i = categories_data(url_categorie)
    #print(i)
    
    #'''
    categories_url = get_category_urls(main_url)
    categories_names = get_category_names(main_url)

    
    for url,names in categories_url,categories_names:
        file = open(names + '.txt', 'w+')
        file.write(str(categories_data(url)))
        file.close()

    #'''



