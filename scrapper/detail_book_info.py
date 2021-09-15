import requests
from bs4 import BeautifulSoup


def get_book_info(url_book):
    response = requests.get (url_book)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.findAll('td')
        universal_product_code = tds[0]

        price_including_tax_raw = tds[2]
        pit1 = price_including_tax_raw.text
        pit2 = pit1.replace('Â£', '')
        price_including_tax = float(pit2)

        price_excluding_tax_raw = tds[3]
        pet1 = price_excluding_tax_raw.text
        pet2 = pet1.replace('Â£', '')
        price_excluding_tax = float(pet2)

        number_available_raw = tds[5]
        number_available_str = str(number_available_raw)
        number_available_incomplete = number_available_str.replace('<td>In stock (','')
        number_available = int(number_available_incomplete.replace(' available)</td>',''))

        titres = soup.findAll('h1')
        titre = titres[0]
    
        descripts = soup.findAll('p')
        descript = descripts[3]

        categories = soup.findAll('a')
        categorie = categories[3]
    
        image = soup.find(class_='item active')
        image_str = str(image)
        image_incomplete_url1 = image_str.replace('<div class="item active">','')
        image_incomplete_url2 = image_incomplete_url1.replace('<img alt="Tipping the Velvet" src="../..', 'http://books.toscrape.com')
        image_incomplete_url3 = image_incomplete_url2.replace('"/>','')
        image_url = image_incomplete_url3.replace('</div>', '')

        rating = product_rating(str(soup.find("p", class_="star-rating")))
    

        informations_livre = {'titre' : titre.text , 'upc' : universal_product_code.text , 'note' : rating , 'categorie' : categorie.text , 'page_url' : url_book , 'image_url' : image_url , 'prix_ht_in_£' : price_excluding_tax, 'prix_ttc_in_£' : price_including_tax , 'stock' : number_available , 'description' : descript.text }
        return informations_livre

def product_rating(rating):
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