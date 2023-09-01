# Tu ćemo sigurno zaradit nešto sitno
# U ovoj simulaciji imamo početni iznos. Najprije uložimo 1 dolar. U slučaju dobitka, sve je super. U slučaju gubitka, ulažemo dvostruko više od prethodnog uloga, kako bi eventualni dobitak pokrio prethodne gubitke i dao neku zaradu. Uvijek na kraju profitiramo, osim ako uspijemo izgubiti apsolutno sve. Simulacija staje nakon prvog dobitka
import random

def rulet_simulacija(pocetni_iznos):
    trenutni_iznos = pocetni_iznos
    ulog = 1  # Počinjemo s ulogom od 1 dolara

    while trenutni_iznos > 0:
        # Simulirajte okretanje ruleta (crno ili crveno)
        ishod = random.choice(['Crno', 'Crveno'])

        # Ako dobijemo, vraćamo uloženi iznos i zarađujemo isti iznos
        if ishod == 'Crveno':
            trenutni_iznos += ulog
            ulog = 1  # Vraćamo se na početni ulog
        # Ako izgubimo, udvostručujemo ulog i smanjujemo trenutni iznos
        else:
            trenutni_iznos -= ulog
            ulog *= 2

        print(f'Ishod: {ishod}, Trenutni iznos: {trenutni_iznos}, Ulog: {ulog}')

        # Ako smo ostvarili dobitak, prekinemo petlju
        if trenutni_iznos >= pocetni_iznos:
            break

    return trenutni_iznos

pocetni_iznos = float(input('Unesite početni iznos: '))
zavrsni_iznos = rulet_simulacija(pocetni_iznos)
print(f'Završni iznos: {zavrsni_iznos}')
