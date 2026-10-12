import random
sekret=random.randint(1,10)
proba=1
maks_proba= 3
zgadlem=False

while proba<=maks_proba and zgadlem==False:
    liczba=int(input("Podaj liczbę od 1 do 10: "))
    if liczba == sekret:
        print ("Brawo zgadłeś")
        zgadlem=True
    elif liczba > sekret:
        print ("Za dużo")
    else:
        print ("Za mało")
    proba+=1

if zgadlem==False:
    print (f"Nie dałeś rady, liczba to {sekret}")
