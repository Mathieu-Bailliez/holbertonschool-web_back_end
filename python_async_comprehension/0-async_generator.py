#!/usr/bin/env python3
"""
Module contenant un générateur asynchrone.

Ce module définit la coroutine async_generator qui produit
10 nombres aléatoires entre 0 et 10, en attendant 1 seconde
de façon asynchrone avant chacun d'eux.
"""

# asyncio : bibliothèque standard pour la programmation asynchrone.
# On s'en sert ici pour asyncio.sleep, un "sommeil" NON bloquant.
import asyncio

# random : bibliothèque standard pour générer des nombres aléatoires.
import random

# AsyncGenerator sert à annoter (décrire) le type de notre fonction.
# AsyncGenerator[float, None] veut dire :
#   - float : le type des valeurs produites par chaque "yield"
#   - None  : on n'envoie aucune valeur au générateur (.asend())
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Produit 10 nombres aléatoires entre 0 et 10, un par seconde.

    À chaque tour de boucle, la coroutine attend 1 seconde sans
    bloquer le programme, puis renvoie (yield) un nombre décimal
    aléatoire. Elle se parcourt avec "async for".
    """
    # range(10) donne 0, 1, ..., 9, donc la boucle fait 10 tours.
    # On écrit "_" car on n'a pas besoin du numéro du tour.
    for _ in range(10):
        # On attend 1 seconde. Le mot "await" signifie :
        # "mets-moi en pause et laisse les autres tâches
        # travailler pendant ce temps".
        await asyncio.sleep(1)

        # random.uniform(0, 10) renvoie un float entre 0 et 10.
        # "yield" renvoie cette valeur à celui qui parcourt le
        # générateur, puis met la fonction en pause jusqu'à la
        # demande de la valeur suivante.
        yield random.uniform(0, 10)
