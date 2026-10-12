import random

for i in range(1,11):
    liczba = random.randint(1,20)
    if liczba%2==0:
        print(f"{liczba} jest liczbą parzystą")
    else:
        print(f"{liczba} jest liczbą nieparzystą")
