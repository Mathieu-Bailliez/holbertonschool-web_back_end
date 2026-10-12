#!/usr/bin/env python3
"""
Ce module montre comment lancer plusieurs coroutines EN MÊME TEMPS.

Rappel des mots importants :
- Une "coroutine" est une fonction déclarée avec "async def".
  Elle peut se mettre en pause (avec "await") pour laisser
  d'autres coroutines travailler pendant qu'elle attend.
- "asyncio" est le module de Python qui gère ces coroutines.
  Il joue le rôle de chef d'orchestre : il décide qui travaille
  pendant que les autres attendent.
"""

# On importe asyncio : c'est l'outil qui fait tourner les coroutines.
import asyncio

# On importe "List" pour pouvoir écrire le type "List[float]",
# qui veut dire : "une liste qui contient des nombres à virgule".
# (Avec Python 3.8, on est obligé de passer par "typing".)
from typing import List

# On récupère la fonction "wait_random" écrite dans la tâche 0.
# On utilise __import__ car le nom du fichier commence par un chiffre
# ("0-basic_async_syntax"), ce qu'un "import" classique refuse.
# Pour rappel, wait_random(max_delay) attend un temps au hasard
# entre 0 et max_delay secondes, puis renvoie ce temps.
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance wait_random n fois en même temps et renvoie la liste
    des temps d'attente, du plus petit au plus grand.

    Paramètres :
        n : le nombre de fois qu'on lance wait_random.
        max_delay : le temps d'attente maximum, en secondes.

    Renvoie :
        Une liste de n nombres à virgule, déjà triés dans l'ordre
        croissant, sans avoir utilisé sort().
    """

    # ÉTAPE 1 : préparer les coroutines, sans les démarrer.
    # Appeler wait_random(max_delay) SANS "await" ne lance rien :
    # cela crée juste une coroutine "prête à partir".
    # On en prépare n et on les range dans une liste.
    coroutines = []
    for _ in range(n):
        # "_" est un nom de variable qu'on utilise quand on n'a pas
        # besoin de la valeur : ici on veut juste répéter n fois.
        coroutines.append(wait_random(max_delay))

    # ÉTAPE 2 : préparer une liste vide pour ranger les résultats.
    delays: List[float] = []

    # ÉTAPE 3 : lancer toutes les coroutines en même temps.
    # asyncio.as_completed() démarre TOUTES les coroutines d'un coup,
    # puis nous les rend une par une, DANS L'ORDRE OÙ ELLES FINISSENT.
    # La plus rapide arrive en premier, la plus lente en dernier.
    for finished in asyncio.as_completed(coroutines):

        # "await" veut dire : "attends le résultat de celle-ci".
        # Pendant cette attente, les autres continuent de tourner.
        delay = await finished

        # On ajoute le temps obtenu à la fin de la liste.
        delays.append(delay)

    # ÉTAPE 4 : renvoyer la liste.
    # Elle est déjà triée, car les coroutines qui attendent le moins
    # longtemps finissent forcément les premières.
    return delays
