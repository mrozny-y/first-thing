import random

wylosowana=random.randint(1,10)
proba=1
liczba=0

while liczba!=wylosowana and proba<=3:
    liczba=int(input("podaj liczbe od 1 do 10: "))
    if liczba==wylosowana:
        print ("brawo, zgadłeś!")
    else:
        if liczba > wylosowana:
            print ("za dużo")
        else:
            print ("za mało")

    proba += 1

if liczba != wylosowana:
    print ("Nie udało się zgadnąć. Wylosowana liczba to:", wylosowana)
