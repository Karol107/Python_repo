# # import requests
# # import json
# # import time
# # from datetime import datetime
# #
# #
# # url = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/'
# #
# # # funkcja pobierająca aktualny kurs dolara
# # def readCurrency(adres):
# #     print("---------------------------------------")
# #     try:
# #         r = requests.get(adres)
# #         data = r.json()
# #         cur = data['rates'][0]['mid']
# #         print("Kurs dolara: ", cur)
# #     except TimeoutException:
# #         print('Blad pozyskania danych')
# #
# # # funkcja mierząca czas wykonania fukcji readCurrency wraz z podaniem aktualnej daty
# # def timeMeasure():
# #     start = time.time()
# #     readCurrency(url)
# #     now = datetime.now()
# #     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# #     print("Data i godzina: ", dt_string)
# #     print ('Czas wykonania zapytania: %.2f sekund' % (time.time() - start))
# #
# # #funckja wywolująca timeMeasure 5 razy co 12 sekund
# # def InterLoop():
# #     for i in range(0,5):
# #         timeMeasure()
# #         time.sleep(15.0)
# #
# # InterLoop()
# #
# #
# #
# #
# #
# #
# # _-------------------------------------------------
# #
#
#
#
#
#
# import requests
# import datetime
# import time
#
#
# def get_currency_to_pln(currency="EUR"):
#     currency = {'base': currency, 'symbols': 'PLN'}
#     r = requests.get('https://api.ratesapi.io/api/latest', params=currency)
#     data = r.json()
#     return data['rates']['PLN']
#
#
# def get_eur_to_pln_time():

#     start = datetime.datetime.now()
#     try:
#         rate = get_currency_to_pln()
#         duration = datetime.datetime.now() - start
#     except:
#         rate = None
#         duration = datetime.datetime.now() - start
#     return rate, duration
#
#
# while True:
#     date = datetime.datetime.now()
#     rate, duration = get_eur_to_pln_time()
#
#     print("------------------------------------------")
#     if rate is None:
#         print("Błąd pozyskiwania danych")
#     else:
#         print('Kurs Euro:',  rate)
#     print('Data i godzina:', str(date))
#     print('Czas wykonania zapytania:', str(duration.microseconds/1000) + 'ms')
#
#     time.sleep(15)




import requests
import json
import time
from datetime import datetime
import csv

file = open('OdczytWaluty.csv', 'w', newline='')
writer = csv.writer(file, delimiter=';')
writer.writerow(["Kurs USD", "Data odczytu", "Godzina odczytu", "Czas wykonania zapytania"])
newline = []

url = 'http://api.nbp.pl/api/exchangerates/rates/a/usd/'

# funkcja pobierająca aktualny kurs dolara
def readCurrency(adres):
    print("---------------------------------------")
    newline.clear()
    try:
        r = requests.get(adres)
        data = r.json()
        cur = data['rates'][0]['mid']
        print("Kurs dolara: ", cur)
        newline.append(cur)
        return newline

    except TimeoutException:
        print('Blad pozyskania danych')
        newline.append('Blad')
        print(newline)


# funkcja mierząca czas wykonania fukcji readCurrency wraz z podaniem aktualnej daty
def timeMeasure():
    start = time.time()
    readCurrency(url)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y")
    hr_string = now.strftime("%H:%M:%S")
    print("Data i godzina: ", dt_string, " ", hr_string)
    newline.append(dt_string)
    newline.append(hr_string)
    zapCzas = time.time() - start
    print ('Czas wykonania zapytania: %.2f sekund' % zapCzas)
    newline.append(zapCzas)
    print(newline)
    writer.writerow(newline)

#funckja wywolująca timeMeasure 5 razy co 2 sekund
def InterLoop():
    for i in range(0,5):
        timeMeasure()
        time.sleep(2.0)

InterLoop()