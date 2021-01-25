stato_capitale = {
'Italia':'Roma',
'Norvegia':'Oslo',
'Austria':'Vienna',
'Cina':'Pechino',
'Egitto':'Il Cairo',
'Svezia':'Stoccolma'
}
stato = input("quale è lo stato di cui vuoi sapere la capitale?")

if stato in stato_capitale:
    capitale = stato_capitale[stato]
    print("La capitale dello stato ", stato," è",capitale )
else:
    print("lo stato non fa parte della lista")