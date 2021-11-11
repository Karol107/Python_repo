# Zadanie domowe modul 5, pobieranie wartosci zlota za 1g w PLN. Author: kk_kontakt@interia.eu

import requests
import json
import time
import datetime
# import pandas as pd

url = 'http://api.nbp.pll/api/cenyzlota/last/30/?format=json'


def get_gold_price():
    r = requests.get(url)
    info = json.loads(r.text)
    get_last_row = info.pop()
    date = get_last_row['data']
    course = get_last_row['cena']
    return course


def actual_hour_and_duration():
    start_duration = datetime.datetime.now()
    get_gold_price()
    duration = datetime.datetime.now() - start_duration
    actual_hour = datetime.datetime.now()
    actual_hour = str(actual_hour.strftime('%d-%m-%Y %H:%M:%S'))
    return actual_hour, duration

# def export_course_to_csv:
#     dict = get_gold_price()
#
#
#     df = pd.DataFrame(dict)
#     df.to_csv('Kursy_walut.csv')


try:
    while True:
        Gold = get_gold_price()
        actual_hour, duration = actual_hour_and_duration()
        print("-" * 15 + '<< source: nbp.pl >>' + "-" * 15, '\nCena 1 g złota:           ', Gold, 'zl'
              , '\nData i godzina:           ',actual_hour,'\nCzas wykonania zapytania: ', duration.microseconds/1000, 'ms')
        time.sleep(15)

except requests.exceptions.Timeout as error:
    print("-" * 15 + '<< source: nbp.pl >>' + "-" * 15, '\nTimeout error',
          '\nData i godzina:           ', actual_hour, '\nCzas wykonania zapytania: ',
          duration.microseconds / 1000, 'ms', '\nReason:\n', error)






















