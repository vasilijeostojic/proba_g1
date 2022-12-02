         #   0      1      2
osoba = ["Sofija", 25, "Python"]
 # 0 ime, 1 godine, 2 smer

 #ime : Sofija
 #godine : 25
 #smer : python

 #osoba[0] - ime
 #osoba["ime"] - ime osobe
 #osoba["godine"] - godine osobe

#kljuc : vrednost
#ime: Sofija             godine: 25        smer: Python
#       0                    1                   2
#     sofija, 25, python
         #kljuc vrednosti
recnik = {"Ime": "Sofija", "godine": 25, "smer": "Python", "aktivan": True}
polaznici = {333: "Petar", 222: "Jovana", 150: "Ana"}

print(recnik)
print(recnik["Ime"])
print(recnik["godine"])
print(recnik["smer"])
print(recnik["aktivan"])


poruke = {"en": "Hello", "sr": "Zdravo", "de": "Hallo"}
jezik = input("Unesite jezik (en/sr/de): " )
if jezik != "en" and jezik != "sr" and jezik != "de":
    print("Dostupni su : en, sr i de")
else:
    print(poruke[jezik])

poruke["it"] = "Bongiorno"

print(poruke)

poruke["sr"] = "Cao"
print(poruke)

for jezik in poruke:
    print(jezik)

for kljuc in poruke:
    print(poruke[kljuc])
    

poeni = {"kate": 800, "tom": 750, "john": 800}
print(poeni)

