# Zadanie domowe modul 5, pobieranie kursu walut EUR. Author: kk_kontakt@interia.eu

import requests
import json
import time
import datetime
import pandas as pd

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=93ba2d6a469cb686077452c399fcd7f2'    # Trial version 30 days only :(


def get_EUR():
    r = requests.get(url)
    data = json.loads(r.text)
    waluty = data['rates']
    PLN = waluty['PLN']  # Euro is a base in this api
    return PLN


def actual_hour_and_duration():
    start_duration = datetime.datetime.now()
    get_EUR()
    duration = datetime.datetime.now() - start_duration
    actual_hour = datetime.datetime.now()
    actual_hour = str(actual_hour.strftime('%d-%m-%Y %H:%M:%S'))
    return actual_hour, duration



while True:
    try:
        PLN = get_EUR()
        actual_hour, duration = actual_hour_and_duration()

        print(actual_hour, duration)
        print("-" * 15 + '<< source: exchangeratesapi >>' + "-" * 15, '\nKurs Euro:                ', PLN
              , '\nData i godzina:           ',actual_hour,'\nCzas wykonania zapytania: ', duration.microseconds/1000, 'ms')

        # export_to_csv()

    except requests.exceptions.ConnectionError as err02:
        print("Error connecting, check url: ", err02)
    except requests.exceptions.HTTPError as err01:
        print("HTTP error: ", err01)
    except requests.exceptions.Timeout as err03:
        print("Timeout error:", err03)
    except requests.exceptions.RequestException as err04:
        print("Error: ", err04)

    # def export_to_csv():  ##zadanie z *, nie mam pomyslu, wymaga dopracowania
dict = get_EUR(), actual_hour_and_duration()
    # dict = {'Kurs z dnia': actual_hour, 'Kurs EUR': PLN}
print(dict)
df = pd.DataFrame(dict)
df.to_csv('Kursy_walut.csv')


    ## wykorzystalem gotowca z gory bo mam wrazenie ze to ponizej nigdy sie nie wykona:
    # except:
    #     if duration.microseconds/1000 > 1000:
    #         print("-" * 15 + '<< EUR >>' + "-" * 15, '\nBlad pobierania danych', '\nData i godzina: ', hour,
    #               '\nCzas wykonania zapytania: ', duration.microseconds / 1000, 'ms')

    time.sleep(15)




















