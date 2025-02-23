print("Dobrodosli u lov na blago.")
print("Nalazis se u tajnom zamku, a pred tobom su 2 puta!!!")
put = int(input("Unesi bilo koji cijeli broj da izaberes put. "))
if put % 2 == 0:
    print("Tvoj broj je paran. Ides na drugi sprat. ")
    vrata = int(input("Ispred tebe se nalase troje vrata. Izaberi 1, 2 ili 3. "))
    if vrata == 1:
        print("Usao si u sobu punu lavova koji su te ubili. Pokusaj ponovo!")
    elif vrata == 2:
        print("Usao si u sobu punih mrava koji su te ubili. Pokusaj ponovo!")
    elif vrata == 3:
        print("Imas srece. Nasao si blago!!!")
elif put % 2 != 0:
    print("Krenuo si niz stepenice i pao u provaliju dje si i umro. Pokusaj ponovo!")
else:
    print("Upisao si nesto pogresno.")
