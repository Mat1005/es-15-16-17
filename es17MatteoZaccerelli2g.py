capitale_stato = {
'Roma':'Italia',
'Oslo':'Norvegia',
'Vienna':'Austria',
'Pechino':'Cina',
'Il Cairo':'Egitto',
'Stoccolma':'Svezia'
}
capitale = input("Quale è la capitale di cui vuoi sapere conoscere lo stato?")

if capitale in capitale_stato:
    stato = capitale_stato[capitale]
    print("La città ",capitale,"è la capitale dello stato ",stato )
else:
    print("La capitale non è nella lista") 