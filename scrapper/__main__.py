import csv
import os

from detail_book_info import get_book_info
from detail_book_url import get_all_books_links
from detail_category_url import get_category_urls_and_names


if __name__ == '__main__':

    main_url = 'http://books.toscrape.com'

    os.mkdir('Script_results')

    for category_url, category_name in get_category_urls_and_names(main_url):
        os.mkdir('Script_results/' + category_name)
        with open('Script_results/' + category_name + '/_' + category_name
                  + '.csv', 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['Titre', 'UPC', 'Note', 'Categorie', 'Page_url',
                          'Image_url', 'Prix_ht_en_£', 'Prix_ttc_en_£',
                          'Stock', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for book_link in get_all_books_links(category_url):
                writer.writerow(get_book_info(book_link))

    print("Script terminé avec succès!")
