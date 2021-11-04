def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")
print("0.Zakoncz")
while True:
    choice = input("Wybierz operację(1/2/3/4/0): ")

    if choice in ('1', '2', '3', '4', '0'):
        if choice == '0':
            print('Zakoncz')
            break
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            dodawanie = num1 + num2
            print('wynik dodawaniato:\n', dodawanie)

        if choice == '2':
            odejmowanie = num1 - num2
            print('wynik odejmowania:\n', odejmowanie)

        if choice == '3':
            mnnozenie = num1 * num2
            print('wynik mnozenia:\n', mnnozenie)

        if choice == '4':
            if num2 == 0:
              print('Pamietaj cholero nie dziel przez "0"!')

            else:
                dzielenie = num1 / num2
                print('wynik dzielenia:\n', dzielenie)



    else:
        print("Błędna wartość, podaj poprawną")