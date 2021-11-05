#obsluga wyjatkow
#wyowlanie:

print(variable) #blad nie zadeklarowana zeminna kotra mozna dodac do wyjatku

#wyjatek:

try:
    wait = WebDriver(driver,5)
    wait.until(ec.visibility_of_element((By.Id, 'test')))
    print('iframe found')

#kiedy brak odpiowiedzie prog. np by sie wywali nie wiadzial bym dlaczego

except TimeoutException:
    print ('There is no iframe')

#dzieki wyjatkowi prog nie wywalil sie lecz przeszedl dalej i widze po print ocb idziemy inna sciezka prog bez jego zakonczenia