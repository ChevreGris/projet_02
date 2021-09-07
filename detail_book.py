import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'

response = requests.get (url)


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



    print('UPC : ' + universal_product_code.text)
    print('PRIX HT : ' + price_including_tax.text)
    print('PRIX TTC : ' + price_excluding_tax.text)
    print('STOCK : ' + number_available.text)

    print('TITRE : ' + titre.text)
    
    print('CATEGORIE : ' + categorie.text)

    print('DESCRIPTION : ' + descript.text)

    #print('URL IMAGE : ' + str(image))
