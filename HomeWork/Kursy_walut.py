#
# funkcja udezajaca pod endpoint:
# strona np https://exchangeratesapi.io/documentation/

# zabezpieczenie przed bledem timeout try/except
# funkcja mierzaca cas trwania zapytania oraz date i godzine w kotrej odbylo sie zapytanie wyprointuj te czasy
# program w petli z interwalem 15 sec


# Przykladowy output:
# -----------------------
# Kurs Euro: cos tam
# Data i Godzina: Data Godzina
# Czas wykonania zapytania: 150msilib
# ------------------------------------
#
# interwal 15s
#
# jelsi time out to:
#
# ---------------------------------
# Blad pozyskania danych
# Data i godzian Data Godzina
# Czas wykonania zapytania 100 000 ms


# zadnie na  6 wygenerowac wykres jako plik csv

# ____________________________________________________

# reuirements:
#
# storna musi odpoiwadac
# zabezpiecznei przed zbyt dlugim zapytnaiem





import requests
import datetime
import json


url = 'http://api.exchangeratesapi.io/v1/latest?access_key=93ba2d6a469cb686077452c399fcd7f2'    # Trial version 30 days only :(
# url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'


# # Pobranie aktualnego kursu
def get_EUR():
    r = requests.get(url)
    data = json.loads(r.text)
    waluty = data['rates']
    PLN = waluty['PLN']  # Euro is a base in this api
    print("-" * 25 + '$$' + "-" * 25, '\nKurs Euro:', PLN)



get_EUR()




#
# print("-" * 50, '\nBlad pozyskania danych    "Request Timeout"','\nData i godzina:            ' 'Date_and_Time',
#       '\nCzas wykonania zapytania: ', 'Data i godzina' ) #"gdy Timeou"g
#
#







#
# try:
#    wait = WebDriverWait(driver, 5)
#    wait.until(ec.visibility_of_element_located((By.ID, "test")))
#    print('iframe found')
#
# except TimeoutException:
#    print('There is no iframe')