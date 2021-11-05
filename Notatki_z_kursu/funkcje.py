# Funkcje to wydzielone fragmenty kody krore mozemy wywolywac wielokrotnie poprzez ich wywolanie
#
# def Moja_pierwsza():
#     print('My first fun.')
#
#
# Moja_pierwsza()   # wywolanie f.


##Funkcja z argumentami:funk(name, jezyk):

#     print('hello ' + name + ' it is your first ' + jezyk)
#
# New_funk('Karol','Python')
# #wynik z konsoli: hello Karol it is your first Python




# def dzielenie(licznik, mianownik):
#
#     if mianownik == 0:
#         print('Pamietaj cholero nie dziel przez zero')
#     else:
#         return  licznik / mianownik
#
# print(dzielenie(1,0))
# print(dzielenie(1,2))


# #funkcja z domyslnymi argumentami
#
# def mojanowa(arg1, arg2, x = 'VW'):
#     return f'{arg1} {arg2} {x}'
#
# print(mojanowa(arg1='auto', arg2='to'))          #wywolanie f





from functools import partial

def devision(x, y):
    return  x / y

divide_by_two = partial(devision,2)

print(divide_by_two(4))
print(divide_by_two(6))
print(divide_by_two(9))