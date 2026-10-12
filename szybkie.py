imie=input("podaj imie: ")
liczba1=int(input("podaj liczbe 1: "))
liczba2=int(input("podaj liczbe 2: "))
wynik=liczba1+liczba2
if wynik>20:
    print(f"witaj {imie}, suma {liczba1} i {liczba2}, czyli {wynik}, jest większa od 20")
else:
    print(f"witaj {imie}, suma {liczba1} i {liczba2}, czyli {wynik}, nie jest większa od 20")
