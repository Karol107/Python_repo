#przykladzie samochodu
# clasa w naszym przypadku bedzie wzorem/ przepisem na samochod
# samochod ma dwa kola silnik kolor kierownice jedzie do przedu etc


#obiketem w tym przypadku nazwać mozemy np Alfa Romeo posiada cechy samochodu lub moze ale nie musi posiadac dodatkowe cechy
#w pogramowaniu obiektowym mozemy stworzyc wiele obiektow tej samej klasy. O tych samych cechach ale rownych nazwach np Alfa Romeo, Fiat, Lambo dla klasy samochod.
#takie obiety są tworzone na podstawie klas, maja swoje wlasciwosci np silnik kolor etc
#oraz np metody jak np jazda do przodu.
# Własciwosci sa zmiennymi zadeklarowanymi wew. klasy
# metody sa funkcjami opisujacymi konkretne dzialania
# sma klasa w takim razie jest zbiorem funkcji i zminnych


class MyfirstClass():
    var1 = 1
    var2 = 2

    def fun(self): #w klasie param self jest obowiazkowy
        print("siema")


object = MyfirstClass()
object.var1 #tutaj mamy objekt i wchodzimy do wew biorac 1 zmienna

object2 = MyfirstClass()
object2.var2 #tutaj mamy objekt i wchodzimy do wew biorac 2 zmienna


object3 = MyfirstClass()
object.fun()


print(object2.var1)
print(object2.var1)
