#jest to biblioteka http apach 2 w python
# dla requewstow http dla pythona
#uzywana do destow API

# CRUD to 3 funkcjonalnosci przy budowania API jak i http

# C -create utworzenie nowych inf
# R read/retrive odczytywanie istniejacych inf  | metoda get
# U update modyfikowanie                        | metoda put
# D delete/destory usuwanie istn inf            | metoda delete

#odpowiedzi HTTP Status Codes

#100
    #iinformacyjne
#200
    #success
#300
    #przekierowania
#400
    #client error
#500
    #server error


import requests
#################statusy odp############
# r = requests.get('https://fabrykatestow.pl') #read wynik z konsoli <Response [200]>
# print(r)

# post = requests.post('http://httpbin.org/post') #<Response [200]>
#
# put = requests.put('http://httpbin.org/post') #<Response [405]>
# delete = requests.delete('http://httpbin.org/post') #<Response [405]>

# print(delete)
############# URL #############


# parameters = {'key1':'value1', 'key2':'value2'}
# r = requests.get('https://fabrykatestow.pl', params = parameters)
# print(r.url)

# udezylismu tu pod adres jw ale z dodatkowymi parametrami value, wynik z konsoli https://fabrykatestow.pl/?key1=value1&key2=value2


########### enkodowanie ###############

parameters = {'key1':'value1', 'key2':'value2'}
r = requests.get('https://fabrykatestow.pl', params = parameters)
print(r.encoding)

# spr enkodowanie na stronie, wynik z consoli: UTF-8