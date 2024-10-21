from physics import *

vyska = 100 # v metrech
vaha = 70 # v kilogramech
vzdalenost = 100000 # v metrech

print(f"Volný pád z {vyska} metrů potrvá {cas_volneho_padu(vyska):.2f} sekund.")
print(f"Pokud na Zemi vážíte {vaha} kg, tak na Měsíci by jste vážil {vaha_na_mesici(vaha):.2f} kg.")
print(f"Rychlostí světla urazíte {vzdalenost} metrů za {jak_dlouho_rychlosti_svetla(vzdalenost):} sekund.")
print(f"Rychlostí zvuku urazíte {vzdalenost} metrů za {jak_dlouho_rychlosti_zvuku(vzdalenost):} sekund.")