from os import write
import requests
from bs4 import BeautifulSoup
import csv

from detail_book_info import get_book_info
from detail_book_url import get_all_books_links
from detail_category_url import get_category_urls_and_names

if __name__ == '__main__':

    main_url = 'http://books.toscrape.com'
    
    for category_url, category_name in get_category_urls_and_names(main_url):
        with open(category_name + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['titre', 'upc', 'note', 'categorie', 'page_url', 'image_url', 'prix_ht_in_£', 'prix_ttc_in_£', 'stock', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for book_link in get_all_books_links(category_url): 
                writer.writerow(get_book_info(book_link))