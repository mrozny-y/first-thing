dol=1
gora=100
trafiona=False

print ("Pomyśl liczbę od 1 do 100.")
print ("Będę próbował ją odgadnąć.")

while trafiona==False:
    srodek=(dol + gora)//2

    print ("Czy twoja liczba to", srodek)
    odpowiedz=input("Wpisz: m - mniejsza, w - większa, t - trafiona: ")

    if odpowiedz == "t":
        print("Zgadłem!")
        dol = gora + 1
        trafiona=True

    elif odpowiedz == "m":
        gora = srodek - 1

    elif odpowiedz == "w":
        dol = srodek + 1
        
