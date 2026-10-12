sekret=7
proba=1
maks_prob=3

while proba<=maks_prob:
    liczba=int(input("Podaj liczbę od 1 do 10."))

    if liczba==sekret:
               print("Brawo zgadłeś.")
    elif liczba < sekret:
                print("Za mało.")
    else:
                print("Za dużo.")
proba+=1

if maks_prob>proba:
    print ("nie dałes rady.")
