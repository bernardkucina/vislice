STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVKJENA_CRKA = 'o'
NAPACNS_CRKA = '-'

#konstante za zamgo
ZMAGA = 'W'
PORAZ = 'X'
bazen = []
with open('besede.txt', encoding='utf-8') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crka=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke