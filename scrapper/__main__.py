import requests
from bs4 import BeautifulSoup

from detail_book_info import get_book_info
#from detail_book_url import get_book_url
from detail_category_url import get_category_url

main_url = 'http://books.toscrape.com'
url_book = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'


urls = get_category_url(main_url)
#print(urls)

#url_book = get_book_url(urls)
info = get_book_info(url_book)
print(info)
