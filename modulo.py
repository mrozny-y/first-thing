wybor=int(input("podaj liczbę"))

if wybor%2==0:
    print ("liczba parzysta")
else:
    print ("liczba nieparzysta")


a=33
b=200
if b>a:
    print ("b jest większa od a")

liczba = 15
if liczba > 15:
    print ("liczba większa od 15")
    print ("co tu się stało")
    if liczba >= 15:
        print ("xxx")
if liczba >= 15:
    print ("yyy")


wiek=int(input("podaj swój wiek"))
if wiek>=18:
    print("jesteś pełnoletni")
    print("możesz wejść na stronę")
else:
    print("nie jesteś pełnoletni")


temperatura=int(input("podaj temperaturze wody"))
if temperatura>100:
    print ("stan gazowy")
elif temperatura<0:
        print ("stan stały")
else:
            print ("stan ciekły")
