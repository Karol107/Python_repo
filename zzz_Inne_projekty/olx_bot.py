#scraping z sieci. Wykorzystywana jest tu biblioteka beautifulsoup4 oraz bs4. Wszedzie tam gdzie nie ma api a trzeba poszperac w html
#opera sie na selektorach css
#bs ogrania tylko wprost z zawartosci html. Jesli storna jest oparta na jS to ta biblioteka sie juz nie nada. Wtedy lepsza bedzie selenium

from bs4 import BeautifulSoup
from requests import get

URL = "https://www.olx.pl/dolnoslaskie/q-dzialka/"

def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(',', '.'))

def parse_page(number):
    # print(f'Pracuje nad strona {number}')
    page = get(f'{URL}?page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer = offer.find('td', class_='bottom-cell')
        location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
        title = offer.find('strong').get_text().strip()
        price = offer.find('p', class_='price').get_text().strip()
        link = offer.find('a')['href']
        print(location, title, price, link)


for page in range(1,28):
    parse_page(page)




