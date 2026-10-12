jacek=[]
piotrek=[]
bartek=[]

#jacek
ocena_jacek=int(input(f"podaj ile masz ocean"))
suma_jacek=0

for i in range(ocena_jacek):
    ocena=int(input("podaj ocene"))
    jacek.append(ocena)
    suma_jacek+=ocena
srednia_jacek=suma_jacek/len(jacek)
#piotrek
ocena_piotrek=int(input("podaj ile masz ocen"))
suma_piotrek=0

for i in range(ocena_piotrek):
    ocena=int(input("podaj ocene"))
    piotrek.append(ocena)
    suma_piotrek+=ocena
srednia_piotrek=suma_piotrek/len(piotrek)

#bartek
ocena_bartek=int(input(f"podaj ile masz ocen"))
suma_bartek=0

for i in range(ocena_bartek):
    ocena=int(input("podaj ocene"))
    bartek.append(ocena)
    suma_bartek+=ocena
srednia_bartek=suma_bartek/len(bartek)
