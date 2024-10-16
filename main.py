from turtle import *
from random import random
from zelvicka import *

# Inicializace prostředí pro želvičku
turtles()

# Nekonečná smyčka pro výběr uměleckých funkcí
while True:
    # Zobrazení možností
    print("1 pro spirálu")
    print("2 pro hvezdičku")
    print("3 pro stromeček")
    print("4 pro překvapení")


    # Uživatelský vstup pro výběr funkce
    state = input("Zadej 1-5 abyste viděli moje umělecké díla, 0 pro vypnutí: ")

    # Ukončení programu při zadání "0"
    if state == "0":
        break

    # Volba 1 - Kreslení N-úhelníku
    elif state == "1":
        home()
        clear()
        spirala()

    # Volba 2 - Kreslení kruhu s želvičkami
    elif state == "2":
        hvezda()

    # Volba 3 - Kreslení domečku jedním tahem
    elif state == "3":
        strom()

    # Volba 4 - Kreslení jednoduchého stromečku
    elif state == "4":
        prekvapeni()

    # Chybný vstup
    else:
        print("Špatný kód.")