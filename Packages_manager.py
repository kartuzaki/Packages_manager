print("Witaj w programie do ładowania paczek!")


ilosc_elementow = int(input("Podaj proszę, ile elementów chcesz wysłać:"))
paczki = []
aktualna_paczka = []

for numer_elementu in range(1, ilosc_elementow + 1):
    waga = int(input("Podaj proszę wagę elementu {}: ".format(numer_elementu)))
    if 1 <= waga <= 10:
        if sum(aktualna_paczka) + waga <= 20:
            aktualna_paczka.append(waga)
        else:
            paczki.append(aktualna_paczka)
            aktualna_paczka = [waga]
    else:
        break

if aktualna_paczka:
    paczki.append(aktualna_paczka)

print("\nPodsumowanie:")
print("Wysłano paczek:", len(paczki))
print("Wysłano kg:", sum(sum(paczka) for paczka in paczki))
suma_pustych_kg = len(paczki) * 20 - sum(sum(paczka) for paczka in paczki)
print("Suma pustych kilogramów:", suma_pustych_kg)
if suma_pustych_kg > 0:
    max_puste_kg = max(suma_pustych_kg for suma_pustych_kg in [20 - sum(paczka) for paczka in paczki])
    indeks_max_pustych_kg = [20 - sum(paczka) for paczka in paczki].index(max_puste_kg)
    numer_paczki_max_pustych_kg = indeks_max_pustych_kg + 1
    print("Najwięcej pustych kilogramów ma paczka {} ({}kg)".format(numer_paczki_max_pustych_kg, max_puste_kg))
