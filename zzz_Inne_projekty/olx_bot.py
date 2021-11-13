#scraping z sieci. Wykorzystywana jest tu biblioteka beautifulsoup4 oraz bs4. Wszedzie tam gdzie nie ma api a trzeba poszperac w html
#opera sie na selektorach css
#bs ogrania tylko wprost z zawartosci html. Jesli storna jest oparta na jS to ta biblioteka sie juz nie nada. Wtedy lepsza bedzie selenium
#import sqlite3 biblioteka sql export do pliku db to otwarcia w darmowym prog DBeaver

from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv #po wywolaniu proramu przechowuje w argv (krotce) wszystkie elementy z którymi jest uruchomiony skrypt

def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(',', '.'))

URL = "https://www.olx.pl/dolnoslaskie/q-dzialka/?search%5Border%5D=filter_float_price%3Aasc&search%5Bfilter_float_price%3Afrom%5D=40000&search%5Bfilter_float_price%3Ato%5D=150000"

db = sqlite3.connect('dane_dzialka_olx.db')
cursor = db.cursor()                            #sqllite3 zwraca metode cursor

if len(argv) > 1 and argv[1] == 'setup':
    cursor.execute('''CREATE TABLE offers (location TEXT, title TEXT, price REAL, link TEXT)''')
    quit()

def parse_page(number):
    # print(f'Pracuje nad strona {number}')
    page = get(f'{URL}?page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):
        footer = offer.find('td', class_='bottom-cell')
        location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
        title = offer.find('strong').get_text().strip()
        price = parse_price(offer.find('p', class_='price').get_text().strip())
        link = offer.find('a')['href']
        cursor.execute('INSERT INTO offers VALUES (?, ?, ?, ?)', (location, title, price, link))
    db.commit()
    # print(location, title, price, link)


for page in range(1,28):
    parse_page(page)




