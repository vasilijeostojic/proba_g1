#pozdravna poruka sa informacijama o datumu
# print("cao!!!")
# print("danasnji datum je 02.12.")

# ime = "ana"
# ime.capitalize()
# print(ime.capitalize())

def prikazi_poruke(): #potpisfunkcije
    #telo funkcije
    print("cao")
    print("danas je 02.12")
    print("ovo je grupa 1")

prikazi_poruke()


def pokreni_motor():
    print("ubacen kljuc")
    print("ukljucen je motor automobila")


pokreni_motor()

def posalji_poruku(nadimak):
    print(f"hello! {nadimak}")


posalji_poruku("vaskeee")




def prikazi_rezultate(ime, broj_poena=0):
    print(f"ime stuednta: {ime}")
    print(f"broj poena: {broj_poena}")



prikazi_rezultate("Vasilije")



def osnovni_racuni(a , b):
    print(f"Rezultat sabiranja: {a} + {b} = {a+b}")
    print(a+b)

osnovni_racuni(724, 104)


def kalkulator(a, b, operacija):
    if operacija == "+":
        print(a+b)
    elif operacija == "-":
        print(a-b)
    elif operacija == "*":
        print(a*b)
    elif operacija == "/":
        if b == 0:
            print("Nije dozvoljeno deljenje sa 0")
        else:
            print(a/b)
    else:
        print("Proverite operaciju (+,-,/,*)")
    

kalkulator(50, 21, "*")





