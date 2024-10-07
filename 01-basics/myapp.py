def main():
    print("Vítejte v tomto... hm... programu?")
    print("Odpovídejte jak chcete, nemám vás jak hlídat")

    jmeno = input("Jak se jmenuješ?")
    print(f"Ahoj, {jmeno}!")

    vek = input("Jak jsi starý?")
    kulatiny = ((int(vek)+10) // 10) * 10
    print(f"Krása, táhne ti na {kulatiny}")

    zvire = input("Kočka či krysa?")
    print(f"Výborná volba! {zvire} je chutnější")

    vyraz = input("Zkus tuto kalkulačku (napište např.: 3*7-4/2+6): ")
    vysledek = eval(vyraz)
    print(f"Výsledek příkladu {vyraz} je {vysledek}.")

    hodnota_pi = 3.14159
    print(f"Věděli jste, že každý čtverec má víc jak tři stěny?")

    # Závěrečná zpráva
    print(f"Děkujeme za Váš ztracený čas, {jmeno}.")

if __name__ == "__main__":
    main()