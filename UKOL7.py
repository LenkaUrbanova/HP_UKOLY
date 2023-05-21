class Auto():    # definice konkretni nove tridy
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Vozidlo je dostupné"
        else:
            return "Vozidlo není dostupné"

    def get_info(self):
        return f"Auto {self.typ_vozidla}, reg. značka {self.registracni_znacka}"

# vytvoření objektů
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

zadany_typ = input("Jaké vozidlo si přejete zapůjčit?")

if zadany_typ == "Peugeot":
    print(peugeot.pujc_auto())
elif zadany_typ == "Škoda":
    print(skoda.pujc_auto())
else:
    print(
        f"Vozidlo '{zadany_typ}' není k dispozici. K dispozici jsou pouze 2 modely: Peugeot, Škoda"
    )

zadany_typ = input("Jaké vozidlo si přejete zapůjčit?")

if zadany_typ == "Peugeot":
    print(peugeot.pujc_auto())
elif zadany_typ == "Škoda":
    print(skoda.pujc_auto())
else:
    print(
        f"Vozidlo '{zadany_typ}' není k dispozici. K dispozici jsou pouze 2 modely: Peugeot, Škoda"
    )