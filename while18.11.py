import random
# sekunde = 10
'''
if sekunde > 0:
    print(sekunde)
sekunde -= 1
if sekunde > 0:
    print(sekunde)
    sekunde -= 1
if sekunde > 0:
    print(sekunde)
    sekunde -= 1
if sekunde > 0:
    print(sekunde)
    sekunde -= 1
if sekunde > 0:
    print(sekunde)
    sekunde -= 1
if sekunde > 0:
    print(sekunde)
    sekunde -= 1
if sekunde > 0:
    print(sekunde)
    sekunde -= 1
if sekunde > 0:
    print(sekunde)

PRIMER NE POZNAVANJA PETLJI

'''

# sekunde = 10

# while sekunde > 0:
#     print(sekunde)
#     sekunde -= 1


# baterija = 90
# while baterija > 0:
#     print("Preostalo vam je", baterija,"posto baterije")
#     baterija -= random.randint(5,15)
# print("Baterija je prazna")



# zivoti = 3

# while zivoti > 0:
#     print("YOU ARE DIE, TRY AGAIN")
#     zivoti -= 1
# print("GAME OVER")

# for zivoti in range(5,0, -1):
#     print("Igra je u toku")

# print("Igra je gotova")

# broj_pokusaja = 7
# poeni = 0


# while broj_pokusaja > 0:
#     vas_broj = int(input("Unesite vas broj: "))
#     srecan_broj = random.randint(1,20)
#     if srecan_broj == vas_broj:
#         print("CESTITAMO OSVOJILI STE 100$, DOBITNI BROJ", vas_broj,)
#         poeni += 1
#     else:
#         print("VISE SRECE DRUGI PUT","Srecan broj jeste", srecan_broj)
#         broj_pokusaja -=1


# for broj in range(1,10):
#     print(broj)
#     if broj == 5:
#         break


# for broj in range(1,10):
#     if broj == 3:
#         continue
#     print(broj)


# for ime in ["Petar","Marko","Jovana","Misko","Ana"]:
#     if ime == "Jovan":
#         print("Jovana", "Pronadjena!")
#         break
#     print(ime)
# else:
#     print("Zavrseno citanje polaznika...")

zbir = 0
while True:
    broj = input("Unesite neki broj: ")

    if broj == "":
        print("Zbir je: ",zbir)
    elif broj.isnumeric():
        zbir += int(broj)
    elif broj == "QUIT":
        exit()
    else:
        print("PROVERITE UNOS!")



    
