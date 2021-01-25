stati = ["Italia","Norvegia","Austria","Cina","Egitto","Svezia"]
Capitali = ["Roma","Oslo","Vienna","Pechino","Il Cairo","Stoccolma"]

stato = input("Quale è lo stato di cui vuoi sapere la capitale?")
if stato in stati:
    capitale = Capitali[stati.index(stato)]
    print("La capitale dello stato ", stato," è ",  capitale)
else:
    print("Lo stato non fa parte della lista")
