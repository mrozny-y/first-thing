import random
liczba=0
licznik_powtorzen=0
while liczba<80:
    liczba=random.randint(1,100)
    licznik_powtorzen+=1
    if liczba%2==0:
        print(f"losowanie nr.{licznik_powtorzen}: {liczba} jest parzysta")
    else:
        print(f"losowanie nr.{licznik_powtorzen}: {liczba} jest nieparzysta")
