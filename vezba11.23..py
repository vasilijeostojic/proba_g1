#          #0       #1  #2
# osoba = ["Marko", 25, "iOs"]
# print(osoba)

# print(osoba[0])
# print(osoba[1])
# print(osoba[2])

'''
for broj in range(7):
    print(broj)


for broj in range(5,20):
    print(broj)

for broj in range(0,11,2):
    print(broj)

PODSETNIK RANGE SENKVENCE
'''

# kurs = "Python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])
# print(kurs[4])
# print(kurs[5])

# print(len(kurs)) #broj_clanova
# print()


#                   #0-5(ukupno 6)
# for indeks in range(0, 6): #(0, len(kurs)-1) ispisivat  ce sve clanove promenjive kurs do poslednjeg
#     print(kurs[indeks])

# ustanova = "IT Academy"
# print(len(ustanova))

# for slovo in range(len(ustanova)-1):
#     print(ustanova[slovo])


# for slovo in ustanova:
#     print(slovo)

'''
tip_korsinika = "admin"
tip_korsinika[0] = "A"
print(tip_korsinika)
NE MUTABILAN
'''

# korisnicko_ime = input("Unesite korisnicko ime: ")


# if korisnicko_ime == "admin1":
#     print("DOBRO DOSLI")
# else:
#     print("NEISPRAVNI PODACI")

# korisnicko_ime


# #AdmiN1 -> admin1
# if korisnicko_ime.lower() == "admin1":
#     print("DOBRO DOSLI")
# else:
#     print("NEISPRAVNI PODACI")

# korisnicko_ime

# tekst = "A*B#*C#D"

# for slovo in tekst:
#     if slovo != "*" and slovo != "#":
#         print(slovo)
# print()
# for x in range(len(tekst)-1):
#     if tekst[x] == "*":
#         print("* je na poziciji", x)
#     elif tekst[x] == "#":
#         print("# je na poziciji", x)
#     else:
#         print(tekst[x])
# print()
# slovo = "ABC"
# print(slovo in tekst) #operator IN proverava da li se neki niz ("ABC") ili slovo nalaze ("A")


# telefoni = ["iPhone11", "Samsung A22", "iPhone 14", "Huawei Mate 50"]
# telefoni[0] = "iPhone 12 Pro" # komanda pomocu koje menjamo odredjenog clana iz list petlje
#print(telefoni[0])


# for telefon in telefoni:
#     print(telefon)

# for indeks in range(len(telefoni)-1):
#     #print(indeks)
#     print(telefoni[indeks])


# #sve dok je broj indeksa manji od rednog broja poslednjeg clana



# indeks = 0
# duzina_liste = len(telefoni)

# while indeks <duzina_liste:
#     print(telefoni[indeks])
#     indeks += 1

# ponuda_smerova = ["python", "php", "ios", "java"]
# zeljeni_smer = input("Unesite smer koji zelite: ")

# for smer in ponuda_smerova:
#     if zeljeni_smer == smer:
#         print("Odabrali ste smer")
#         break
#     else:
#         print("Nemamo ovaj smer")



# ponuda_smerova = ["python", "php", "ios", "java"]
# ponuda_smerova.append("c#")

# print(ponuda_smerova)
'''
proba = []
proba.append(5)
proba.append("Hello")
print(proba)
#proba.clear()
#print(proba)
#proba.remove(5)
print(proba)
#proba.pop(0)
print(proba)
#del proba [0]
print(proba)

*************** NACINI ZA UKLANJANJE NEZELJENE VELICINE *****************

'''

# laptopovi = ["acer", "dell", "macbook"]

# for i in range(len(laptopovi)):
#     print(laptopovi[i])




# for vrednost in laptopovi:
#     print(vrednost)


# for i, v in enumerate(laptopovi):
#     print("Indeks: ", i, "Vrednost: ", v)

# termini = ["ponedeljak", "sreda", "petak"]

# for x in range(len(termini)):
#     if "utorak" != termini[x]:
#         print("Dodajte i utorak u spisak")
#     print(termini[x])

# if "utorak" in termini:
#     print("Utorak je medju terminima")
# else:
#     print("Dodajte i utorak")

#if not "utorak" in termini:


# smerovi = ["python", "php", "ios", "java", "c#", "fronted", "androdi"]

# promocija = smerovi[1:4]
# print(promocija)

# korisnici = ["petar", "jovana", "marija", "vladimir", "milos", "katarina"]
# pobednici = korisnici[0:3]
# print(pobednici)
# pobednici.clear()

# for i in range(len(korisnici)):
#     if i == 0 or i ==1 or i==2:
#         pobednici.append(korisnici[i])

# print(pobednici)

# brojevi = [10, 22, 3, 11, 5, 4, 1, 8]

# parni = []

# neparni = []

# for broj in brojevi:
#     if broj % 2 == 0:
#         parni.append(broj)
#     else:
#         neparni.append(broj)

# print(parni)
# print(neparni)

# parni.append(broj) if broj % 2 == 0 else neparni.append(broj) drugi nacin ternarni operator


# rec = input("Unesite rec: ")
# pocetni_indeks = 0
# krajnji_indeks = len(rec)-1
# palindrom = True

# '''
# rec[0] == rec[14]      
# rec[1] == rec[13]
# rec[2] == rec[12]

# '''

# while pocetni_indeks < krajnji_indeks:
#     if rec[pocetni_indeks] != rec[krajnji_indeks]:
#         print("Nije palndrom")
#         palindrom = False
#         break
#     pocetni_indeks += 1
#     krajnji_indeks -= 1
# else:
#     print("Jeste palindrom")

# # print ("Rec", rec, ("Jeste" if palindrom else "nije"), palindrom") rijesiti gresku kuci

kursevi = ["python", "ios", "desing"]

#unos kursa input
#provera da li postoji u listi kursevi (in)
#append
#svaki put nakon unosa ili poruke ispisati listu kurseva

zeljeni_kurs = input("Unesite kurs koji zelite da pronadjete: ")
for kurs in kursevi:
    if zeljeni_kurs == kurs:
        print("Vec postoji", kursevi)
        continue
    else:
        kursevi.append(zeljeni_kurs)
