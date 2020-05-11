import vislice

def izpis_poraza(igra):
    return  f'IZGUBIL SI , GESLO JE BILO: {igra.geslo}'

def izpis_poraza(igra):
    return f'ZMAGAL SI, GESLO JE BILO: {igra.geslo},' +
     f'POTREBOVAL SI {len(igra.napacne_crke())} UGIBOV'

def izpis_igra(igra):
    text = (
        f'Stanje gesla: {igra.praviln_del_gesla()} /n '
        f'Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak(} možnosti za napako'

    )

    return text

def zahtevaj_vnos():
    return input('Vpiši naslednjo črko')

def pozeni_umesnik():
    #Naredimo novo igro
    trenutna_igra = model.nova_igra()

    while True:
        print(izpis_igra(trenitna_igra))

        crka = zahtevaj_vnos()
        rezultat = trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            break
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            break

pozeni_umesnik()
