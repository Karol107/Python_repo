# Lekcja 2

def function():
    print('My first function')

def function_new(name, language):
    print('Hello' + name + 'it is four first' + language + 'function')

function_new('Paul','Python')


def divide(dividend, divisor):
    if(divisor == 0):
        return 0
    else:
        return dividend / divisor

print(divide(5,0))
print(divide(10,2))

def my_function(arg1, arg2='Romeo'):
    return f'{arg1} {arg2}'

print(my_function(arg1="Alfa"))

from functools import partial

def division(x, y):
    return x / y

divide_by_two = partial(division, 2)

print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))

# Lekcja 3

class MyFirstClass():
    variable_uno= 1
    variable_duo = 2
    def function(self):
        print("Hello world")

object = MyFirstClass()

object = MyFirstClass()
object.variable_uno
print(object.variable_uno)

object = MyFirstClass()
object.variable_uno
object_2 = MyFirstClass()
object_2.variable_uno
print(object.variable_uno)
print(object_2.variable_uno)

object.function()


# Lekcja 5

try:
   wait = WebDriverWait(driver, 5)
   wait.until(ec.visibility_of_element_located((By.ID, "test")))
   print('iframe found')

except TimeoutException:
   print('There is no iframe')


# Lekcja 6

import requests

r = requests.get('https://fabrykatestow.pl')

print(r)

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")

parameters = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("https://fabrykatestow.pl", params=parameters)
print(r.url)


import requests

r = requests.get('https://fabrykatestow.pl')

print(r.text)
print(r.encoding)
print(r.json)



