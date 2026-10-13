#!/usr/bin/env python3
"""
Module utilisant une compréhension asynchrone.

Ce module définit la coroutine async_comprehension qui collecte
les 10 nombres aléatoires produits par async_generator dans une
liste, puis renvoie cette liste.
"""

# List permet d'annoter le type de retour : List[float] veut dire
# "une liste qui contient des nombres décimaux (float)".
from typing import List

# Le nom du fichier commence par un chiffre ("0-..."), donc on ne
# peut pas écrire "import 0-async_generator" (erreur de syntaxe).
# On utilise donc __import__ avec le nom du fichier sous forme de
# texte, puis on récupère la fonction async_generator qu'il contient.
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires grâce à une compréhension async.

    La compréhension parcourt async_generator avec "async for" et
    place chaque valeur reçue dans une liste, qui est ensuite
    renvoyée. L'exécution dure environ 10 secondes.
    """
    # Lecture de la ligne ci-dessous, de droite à gauche :
    #   - async_generator() : on crée le générateur asynchrone
    #   - async for nombre in ... : on récupère ses valeurs une par
    #     une, en attendant (sans bloquer) que chacune soit prête
    #   - [nombre ...] : on range chaque "nombre" dans une liste
    # Équivalent long :
    #     resultat = []
    #     async for nombre in async_generator():
    #         resultat.append(nombre)
    #     return resultat
    return [nombre async for nombre in async_generator()]
