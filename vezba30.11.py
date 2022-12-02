
# # brojevi = [2, 7, 5, 1, 4, 3, 9]
# # duzina_liste = len(brojevi)
# # print(duzina_liste)
# # while True:
# #     zamenjena_mesta = False
# #     for i in range(1, duzina_liste):
# #         if brojevi [i] < brojevi [i-1]:
# #             privremeno = brojevi [i]
# #             brojevi [i] = brojevi [i-1]
# #             brojevi [i-1] = privremeno
# #             zamenjena_mesta = True
# #     if zamenjena_mesta == False:
# #         #if not zamenjena mesta == False
# #         break
# # print(brojevi)


# # proizvodi = ["Telefon", "TV", "Kompjuter"]
# # cijene = [155.95, 180.35, 199.99]

# # # proizvodi[0] cijene[0]
# # # proizvodi[1] cijene[1]    
# # # proizvodi[2] cijene[2]

# # for x in range(len(proizvodi)):
# #     print("Naziv: ", proizvodi[x], "Cijena: ", cijene[x])

# # ime = "Sofija"
# # poruka = f"Cao, {ime}!!!"

# # print(poruka)



# #proizvodi = ["telefon", "laptop", "tablet"]

# telefoni = ["iphone", "samsung", "huawei"]
# laptopovi = ["mackbook", "acer", "dell"]
# tableti = ["ipad", "xiaomi", "samsung"]

# proizvodi = [ 
#                 ["iphone", "samsung", "huawei"],
#                 ["mackbook", "acer", "dell"],
#                 ["ipad", "xiaomi", "samsung"]
#             ]
# print(proizvodi[0][0])

# # for grupa_prozivoda in proizvodi:
# #     print(grupa_prozivoda)
# #     for proizvod_pojedinacno in grupa_prozivoda:
# #         print(proizvod_pojedinacno)

# for kategorija_proizvoda in proizvodi:
#     for prozivod in kategorija_proizvoda:
#         print(prozivod)

# python22 = [
#      ["marija", "jovana", "marko", "petar"],
#      ["katarina", "aleksa", "sofija", "milica"]
# ]

# for grupa in python22:
#     for ime in grupa:
#         print(ime)

# for i in range(len(python22)):
#     print(python22[i])
#     for y in range(len(python22[i])):
#         print(python22[i][y])

# osoba = ("Sofija", 30, True)
# print(osoba[0])

# ime, godine, aktivan = osoba
# print(ime, godine, aktivan)

# redni_brojevi = (1,)

# osoba = ("Katarina",)

# br = [1, 2, 3]
# print(br.pop())
# print(br)

# br.pop(0)

# print(br.pop(0))



# biblioteka = [
#     ["Uvod u Python", "LinkGroup", 123]
#     ]


# while True:


# #komande:
# # 1 unos knjige - append
# # 2 prikaz
# # 3 brisanje
#     print("Opcija 1 - unost, 2 - prikaz, 3 - brisanje")
#     komanda = int(input("Unesite komandu: "))

#     if komanda == 1:
#         naslov = input("Unesite naslov: ")
#         autor = input("Unesite ime autora: ")
#         isbn = input("Unesite isbn: ")
#         knjiga = [naslov, autor, isbn]
#         biblioteka.append(knjiga)
#         print("Uspesno dodata knjiga")
#         print(biblioteka)
#     elif komanda == 2:
#         for knjiga in biblioteka:
#             for informacija in knjiga:
#                 print(informacija)
#         print("-----------------")
#     elif komanda == 3:
#         isbn_za_brisanje = input("Unesite isbn knjige: ")
#         for knjiga in biblioteka:
#             for informacija in knjiga:
#                 if informacija == isbn_za_brisanje:
#                     biblioteka.remove(knjiga)
#     elif komanda > 3:
#         break



