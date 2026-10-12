import random
szanse=0
odp=0
imie=input("podaj swoje imię: ")
print(f"Witaj {imie}!")
liczba1=random.randint(1,20)
liczba2=random.randint(1,20)
wynik=liczba1*liczba2
while odp!=wynik and szanse <=3:
    odp=int(input(f"Ile wynosi {liczba1} x {liczba2}?: "))
    szanse+=1
    if odp==wynik:
        print("Brawo! zgadłeś!")
    else:
        print("Zła odpowiedź, jeszcze raz.")

if szanse==1:
        print("Zgadłeś za pierwszym razem, otrzymujesz ocenę 6.")
else:      
if szanse==2:
        print("Zgadłeś za drugim razem, otrzymujesz ocenę 4.")
else:
    if szanse==3:
        print("Zgadłeś za trzecim razem, otrzymujesz ocenę 2.")
if odp!=wynik:
    print(f"Nie dałeś rady obliczyć. Poprawnym wynikiem jest {wynik}. Otrzymujesz ocenę 1")
    
        
