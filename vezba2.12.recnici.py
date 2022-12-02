# selekcija = {"drzava": "Srbija",
#     "boja_dresa": ["crvena", "bela"],
#     "broj_pobeda": 1, 
#     "igraci": ["Jovic", "Mitrovic", "Grujic", "Tadic"]
#             }

# for i in selekcija:
#     #print(i, selekcija[i])
#     print(f"{i.capitalize()}:{selekcija[i]}")

# for(kljuc, vrednost) in selekcija.items():
#     if kljuc == "boja_dresa":
#         print("prodji kroz ovu listu", vrednost)
#         for boja in vrednost:
#             print(f"boja dresa: {boja}")
#     elif kljuc == "igraci":
#         for igrac in vrednost:
#             print(f"igrac:{igrac}")
#     print(f"{kljuc}:{vrednost}")

ucesnici = {
    "SRB": {"drzava": "Srbija",
    "boja_dresa": ["crvena", "bela"],
    "broj_pobeda": 1, 
    "igraci": ["Jovic", "Mitrovic", "Grujic", "Tadic"]},
    "FRA":{"drzava": "Francuska",
    "boja_dresa": ["plava", "bela"],
    "broj_pobeda": 2, 
    "igraci": ["Mbappe", "Pogba", "Benzema", "Coman"]},
    "SWI": {"drzava": "Svajcarska",
    "boja_dresa": ["crvena", "bela"],
    "broj_pobeda": 1, 
    "igraci": ["Zommer", "Akanji", "Saciri"]}
        }
print("*******************************************")
for (oznaka, detalji) in ucesnici.items():
    #print(oznaka) # skracenica string kljuc
    #print(detalji) # info o selekciji, recnik
    for (kljuc, vrednost) in detalji.items():
        if kljuc == "boje":
            for boja in vrednost:
                print(f"boja: {boja}")
        elif kljuc == "igraci":
            for igrac in vrednost:
                print(f"igrac: {igrac}")
        else:
            print(f"{kljuc.capitalize()}: {vrednost}")
    print("*******************************************")


automobili = {
    "BG-123" : {
        "marka" : "mercedes",
        "model" : "cls",
        "godiste" : 2018,
        "tip_goriva": "benzin"
    },
    "BG-213" : {
        "marka" : "bmw",
        "model" : "x5",
        "godiste" : 2015,
        "tip_goriva": "benzin"
    },
    "BG-321" : {
        "marka" : "audi",
        "model" : "s3",
        "godiste" : 2020,
        "tip_goriva": "benzin"
    }
}
# print("*******************************************")
# for (registracija, informacije) in automobili.items():
#     for (detalj, vrednosti) in informacije.items():
#         if detalj == "marka":
#             for marka in informacije:
#                 print(f"marka: {marka}")
#         elif detalj == "model":
#             for model in informacije:
#                 print(f"model: {model}")
#         elif detalj == "godiste":
#             for godiste in informacije:
#                 print(f"godiste: {godiste}")
#         elif detalj == "tip_goriva":
#             for tip_goriva in informacije:
#                 print(f"tip_goriva: {tip_goriva}")
#         else:
#             print(f"{detalj.capitalize()}: {vrednost}")

# print("*******************************************")  

for(registracija, informacije) in automobili.items():
    for(kljuc, vrednost) in informacije.items():
        if kljuc == "marka":
            print(f"Marka ovog automobila je: {vrednost}")
        print(f"{kljuc.capitalize()}:{vrednost}")
    print("***********************")