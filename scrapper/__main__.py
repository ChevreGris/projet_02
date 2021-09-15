import requests
from bs4 import BeautifulSoup

from detail_book_info import get_book_info
from detail_book_url import get_book_url
from detail_category_url import get_category_urls

if __name__ == '__main__':

    main_url = 'http://books.toscrape.com'
    url_categories = 'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html'
    url_book = 'http://books.toscrape.com/catalogue/the-grownup_546/index.html'
    


    test_url = get_book_url(url_categories)
    print(test_url)

    #urls = get_category_urls(main_url)
    #print(urls)


    #url_book = get_book_url(urls)
    
    
    #info = get_book_info(url_book)
    #print(info)
