# Description
# Zadanie domowe modul 5, pobieranie wartosci zlota. Cena za 1g w PLN. Author: kk_kontakt@interia.eu

import requests
import json
import time
import datetime
import pandas as pd

url = 'http://api.nbp.pl/api/cenyzlota/last/30/?format=json'

# Po nitce do klębka. Dość laickie podejscie, czy mogłbyś zaproponować swoja wersje podobnej funkcji? jak ty bys to zrobil?
def get_gold_price():
    r = requests.get(url)
    info = json.loads(r.text)
    get_last_row = info.pop()
    date = get_last_row['data']
    course = get_last_row['cena']
    return course, date


def actual_hour_and_duration():
    start_duration = datetime.datetime.now()
    get_gold_price()
    duration = datetime.datetime.now() - start_duration
    actual_hour = datetime.datetime.now()
    actual_hour = str(actual_hour.strftime('%d-%m-%Y %H:%M:%S'))
    return actual_hour, duration


def gold_course_to_csv():
    r = requests.get(url)
    export_list = json.loads(r.text)
    df = pd.DataFrame(export_list)
    df.to_csv('Kurs_zlota.csv')


try:
    while True:
        Gold, date = get_gold_price()
        actual_hour, duration = actual_hour_and_duration()
        print("-" * 15 + '<< source: nbp.pl >>' + "-" * 15, '\nCena 1 g złota:           ', Gold, 'zl'
              , '\nData i godzina:           ', actual_hour, '\nCzas wykonania zapytania: ',
              duration.microseconds / 1000, 'ms')
        gold_course_to_csv()
        time.sleep(15)

except requests.exceptions.Timeout as error:
    actual_hour, duration = actual_hour_and_duration()
    print("-" * 15 + '<< source: nbp.pl >>' + "-" * 15, '\nTimeout error',
          '\nData i godzina:           ', actual_hour, '\nCzas wykonania zapytania: ',
          duration.microseconds / 1000, 'ms', '\nReason:\n', error)
