# OVO NEMA SMISLA, AKO SVAKI PUT ULAŽEMO MANJE, ONDA NAM DOBITAK NIJE GARANTIRAN

# U ovoj simulaciji uvijek ulažemo polovicu početnog iznosa
import random

def rulet_simulacija(pocetni_iznos):
    trenutni_iznos = pocetni_iznos
    broj_oklada = 0

    while trenutni_iznos > 0:
        # Simulirajte okretanje ruleta (crno ili crveno)
        ishod = random.choice(['Crno', 'Crveno'])

        # Računamo polovicu trenutnog iznosa kao ulog
        ulog = trenutni_iznos / 2

        # Ako dobijemo, vraćamo uloženi iznos i zarađujemo isti iznos
        if ishod == 'Crno':
            trenutni_iznos += ulog
        # Ako izgubimo, gubimo ulog
        else:
            trenutni_iznos -= ulog

        broj_oklada += 1
        print(f'Oklada {broj_oklada}: Ishod: {ishod}, Trenutni iznos: {trenutni_iznos}, Ulog: {ulog}')

        # Ako smo ostvarili dobitak, prekinemo petlju
        if trenutni_iznos >= (pocetni_iznos * 2):
            break

    return trenutni_iznos, broj_oklada

pocetni_iznos = float(input('Unesite početni iznos: '))
zavrsni_iznos, broj_oklada = rulet_simulacija(pocetni_iznos)
print(f'Završni iznos: {zavrsni_iznos}')
print(f'Broj oklada: {broj_oklada}')
