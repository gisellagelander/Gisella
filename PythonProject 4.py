#Moduuli 04 Alkuehdollinen toistorakenne

1
luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

#2
  tuuma = float(input("Anna tuumat (negatiivinen lopettaa):"))

    while tuuma >= 0:
       cm = tuuma * 2.54
        print(f"{tuuma} tuuma = {cm:.2f} cm")
        tuuma = float(input("anna tuumat (negatiivinen lopettaa): "))

    print("Ohjelma on loppunut.")

#3

luvut = []

while True:
    syote = input("Anna luku väliltä 10-100 (tyhjä lopettaa): ")
    if syote == "":
        break
    luku = int(syote)
    if 10 <= luku <= 100:
     luvut.append(luku)
    else:
        print("virhe luvun täytyy olla väliltä 10-100!")

    if len(luvut) > 0:
        print("pienin", min(luvut))
        print("suurin luku:", max(luvut))
    else:
        print("ei kelvollista lukua")

#4

import random

salainen = random.randint(1,10)
yritykset = 0

while True:
    arvaus = int(input("arvaa luku väliltä 1-10: "))
    yritykset += 1

    if arvaus < salainen:
        print("Liian pieni arvaus")
    elif arvaus > salainen:
        print("Liian suuri arvaus")
    else:
        print("oikein")
        if yritykset == 4:

          print("arvasit oikein 4: yrityksellä.")
        else:
            print(f"arvasit oikein yrityksellä")
        break
