import requests
from bs4 import BeautifulSoup


def get_book_info(url_book):
    # fonction qui retourne toutes les infos demandées d'une page d'un livre.

    response = requests.get(url_book)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.findAll('td')

        universal_product_code = tds[0].text
        price_including_tax = float(tds[2].text.replace('Â£', ''))
        price_excluding_tax = float(tds[3].text.replace('Â£', ''))
        number_available_str = str(tds[5])
        number_available_int = int(number_available_str.replace(
                '<td>In stock (', '').replace(' available)</td>', ''))
        title = soup.findAll('h1')[0].text
        description = soup.findAll('p')[3].text
        category = soup.findAll('a')[3].text
        image = soup.find(class_='item active').find('img')
        image_url = image['src'].replace(
                '../../', 'https://books.toscrape.com/')
        rating = product_rating(str(soup.find("p", class_="star-rating")))

        download_image(image_url, title, category)

        book_data = {'Titre': title, 'UPC': universal_product_code,
                     'Note': rating, 'Categorie': category,
                     'Page_url': url_book, 'Image_url': image_url,
                     'Prix_ht_en_£': price_excluding_tax,
                     'Prix_ttc_en_£': price_including_tax,
                     'Stock': number_available_int, 'Description': description}
        return book_data


def product_rating(rating):
    # fonction qui retourne la note d'un livre en int.

    if ("One") in rating:
        rating = 1
    elif ("Two") in rating:
        rating = 2
    elif ("Three") in rating:
        rating = 3
    elif ("Four") in rating:
        rating = 4
    elif ("Five") in rating:
        rating = 5
    else:
        rating = None
    return rating


def download_image(image_url, title, category_name):
    # fonction qui telecharge l'image de chaques livres

    response = requests.get(image_url)

    file = open('Script_results/' + category_name + '/'
                + title.replace('/', ' ').replace('\\', ' ').replace(':', ' ')
                .replace('*', ' ').replace('"', ' ').replace('?', ' ')
                .replace('<', ' ').replace('>', ' ').replace('|', ' ')
                 + '.jpg', "wb")
    file.write(response.content)
    file.close()
