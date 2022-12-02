blacklist = ("potter", "john", "sally")
users = []
while True:
    ime = input("Unesite ime : ")
    if ime == "q":
        break
    elif ime in blacklist:
            print("Nedozvoljen pristup")
    else:
            users.append(ime)

            print(users)
    
