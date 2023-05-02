import math

def over_cislo(cislo):
    if len(cislo) == 9 or (len(cislo) == 13 and cislo[0:4] == "+420"):
        return True
    cislo = (input("Napiš tel.číslo:"))   
    else:
    return False
# cislo = (input("Napiš tel.číslo:"))   
    
def cena_zpravy(zprava):
    if len(zprava) % 180 == 0:
        cena = (len(zprava) // 180) * 3
    else:
        cena = ((len(zprava) // 180) + 1) * 3




    






