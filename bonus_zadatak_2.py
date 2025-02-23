proizvod = float(input("Unesite broj proizvoda za kupovinu: "))
cijena = float(input("Unesite cijenu po komadu: "))
provizija = float(input("Unesite proviziju (%) za kupovinu: "))
prodajna_cijena = float(input("Unesite očekivanu prodajnu cijenu po komadu: "))
print("\n")


procenat = provizija/ 10

ukupan_trosak = proizvod * cijena + (cijena * procenat)
prodajna_vrijednost = proizvod * prodajna_cijena
moguca_zarada = prodajna_vrijednost - ukupan_trosak


print(f"Ukupan trošak kupovine: {ukupan_trosak}e. ")
print(f"Moguća prodajna vrijednost: {prodajna_vrijednost}")

if prodajna_vrijednost > ukupan_trosak:
    print(f"Moguća zarada: {moguca_zarada}")
    print(f"Vrijedi pokušati, moguća zarada je {moguca_zarada}")
elif prodajna_vrijednost < ukupan_trosak:
    print("Nema zarade, bolje pričekaj.")
#  da napomenem da je zadatak bonus2 duplo laksi nego zadatak bonus1
