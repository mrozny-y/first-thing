import math
dlugosc=float(input("podaj długość pokoju: "))
szerokosc=float(input("podaj szerokość pokoju: "))
wysokosc=float(input("podaj wysokość pokoju: "))
sciana1=wysokosc*szerokosc
sciana2=wysokosc*dlugosc
powierzchnia=sciana1*2+sciana2*2
cenafarby=15
wydajnosc=13
ilelitrow=powierzchnia/wydajnosc
wynik1=round(ilelitrow, 1)
potrzebafarby=ilelitrow*cenafarby
wynik2=round(potrzebafarby)

                      
print(f"powierzchnia ścian: {powierzchnia} m²")                
print(f"ile litrów farby potrzeba: {wynik1} l")
print(f"koszt potrzebnej farby: {wynik2} zł")
