STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVKJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

#konstante za zamgo
ZMAGA = 'W'
PORAZ = 'X'
bazen_besed = []
with open('besede(1).txt', encoding='utf-8') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crka=None):
        self.geslo = geslo.lower()
        if crka is None:
            self.crke = []
        else:
            self.crke = crka.lower()
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True
    

    