import requests
import json
import time
import datetime

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=93ba2d6a469cb686077452c399fcd7f2'    # Trial version 30 days only :(
# url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'


def get_EUR():
    start_duration = datetime.datetime.now()
    r = requests.get(url)
    data = json.loads(r.text)
    duration = datetime.datetime.now() - start_duration
    waluty = data['rates']
    PLN = waluty['PLN']  # Euro is a base in this api
    return PLN, duration

def actual_hour():
    actual_hour = datetime.datetime.now()
    actual_hour = str(actual_hour.strftime('%d-%m-%Y %H:%M:%S'))
    print('Data i godzina: ', actual_hour)
    return actual_hour

while True:
    try:
        PLN, duration = get_EUR()
        hour = actual_hour()
        print("-" * 15 + '<< EUR >>' + "-" * 15, '\nKurs Euro:      ', PLN,'\nData i godzina: ',hour,
              '\nCzas zapytania: ', duration.microseconds/1000, 'ms')

    except requests.exceptions.ConnectionError as err02:
        print("Error connecting check url: ", err02)
    except:                                                                                             #mam watpliwosc ze to sie nigdy nie wykona
        if duration.microseconds/1000 > 1000:
            print("-" * 15 + '<< EUR >>' + "-" * 15, '\nBlad pobierania danych', '\nData i godzina: ', hour,
                  '\nCzas zapytania: ', duration.microseconds / 1000, 'ms')


    time.sleep(15)






















