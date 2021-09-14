import requests
from bs4 import BeautifulSoup


def product_rating(rating):
    if ("One") in rating:
        rating = "1/5"
    elif ("Two") in rating:
        rating = "2/5"
    elif ("Three") in rating:
        rating = "3/5"
    elif ("Four") in rating:
        rating = "4/5"
    elif ("Five") in rating:
        rating = "5/5"
    else:
        rating = None
    return rating




def get_book_info(url_book):


    response = requests.get (url_book)


    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.findAll('td')
        universal_product_code = tds[0]
        price_including_tax = tds[2]
        price_excluding_tax = tds[3]
        number_available = tds[5]

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
    

        print('Page url : ' + url_book)
        print('UPC : ' + universal_product_code.text)
        print('PRIX HT : ' + price_including_tax.text)
        print('PRIX TTC : ' + price_excluding_tax.text)
        print('STOCK : ' + number_available.text)
        print('TITRE : ' + titre.text)
        print('CATEGORIE : ' + categorie.text)
        print('DESCRIPTION : ' + descript.text)
        print('url image ' + image_url)
        print('Note : ' + rating)

        #return{titre,categorie,url_book,universal_product_code,price_excluding_tax,price_including_tax,number_available,descripts,image_url,rating}
        #print(titre.text + ',' + categorie.text + ',' + url_book + ',' + universal_product_code.text + ',' + price_excluding_tax.text + ',' + price_including_tax.text + ',' + number_available.text + ',' + descripts.text + ',' + image_url + ',' + rating)

#comment faire sortir le resultat sur une ligne, et séparé par une virgule?
