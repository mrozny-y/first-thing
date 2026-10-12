print("--- System postaci ---")
print("Tworzenie nowego bohatera")

imie = str(input("Podaj nazwę bohatera: "))
poziom = 1
zdrowie = 100
obrażenia = 12.5
zyje = True

zdrowie= 100+ poziom*10
obrazenia=10+ poziom*5

typPrzeciwnika="cyklop"
zyciePrzeciwnika= 60
atakPrzeciwnika= int(20)

print("1 rycerz 2 assassin 3 mag")
wybor=int(input("wybierz klasę postaci"))
if wybor==1:
    zdrowie=300
    atak=80
elif wybor==2:
        zdrowie=100
        atak=150
elif wybor==3:
        zdrowie=150
        atak=100

print(f"Imie: {imie}")
print(f"LVL: {poziom}")
print(f"HP: {zdrowie}")

print(f"{imie} spotkał {typPrzeciwnika}a i stracił {atakPrzeciwnika} HP")
zdrowie=zdrowie-atakPrzeciwnika
print (f"{zdrowie}")

