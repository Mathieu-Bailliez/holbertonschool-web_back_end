#!/usr/bin/env python3
"""
Ce module lance plusieurs Tasks EN MÊME TEMPS.

C'est presque une copie de wait_n (tâche 1), avec une seule
différence : au lieu d'appeler wait_random, on appelle
task_wait_random (tâche 3), qui renvoie une Task déjà lancée.
"""

# On importe asyncio : il gère les coroutines et les Tasks.
import asyncio

# On importe "List" pour écrire le type "List[float]",
# qui veut dire : "une liste qui contient des nombres à virgule".
# (Avec Python 3.8, on est obligé de passer par "typing".)
from typing import List

# On récupère la fonction "task_wait_random" écrite dans la tâche 3.
# Pour rappel, task_wait_random(max_delay) crée une Task qui attend
# un temps au hasard entre 0 et max_delay secondes, puis renvoie
# ce temps.
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance task_wait_random n fois en même temps et renvoie la liste
    des temps d'attente, du plus petit au plus grand.

    Paramètres :
        n : le nombre de Tasks à lancer.
        max_delay : le temps d'attente maximum, en secondes.

    Renvoie :
        Une liste de n nombres à virgule, déjà triés dans l'ordre
        croissant, sans avoir utilisé sort().
    """

    # ÉTAPE 1 : créer les Tasks.
    # SEULE DIFFÉRENCE avec wait_n : on appelle task_wait_random
    # au lieu de wait_random.
    # Chaque appel crée une Task qui DÉMARRE TOUT DE SUITE en
    # arrière-plan (contrairement à une simple coroutine).
    tasks: List[asyncio.Task] = []
    for _ in range(n):
        # "_" veut dire : on n'a pas besoin du numéro du tour,
        # on veut juste répéter n fois.
        tasks.append(task_wait_random(max_delay))

    # ÉTAPE 2 : préparer une liste vide pour ranger les résultats.
    delays: List[float] = []

    # ÉTAPE 3 : récupérer les résultats dans l'ordre d'arrivée.
    # asyncio.as_completed() nous rend les Tasks une par une,
    # DANS L'ORDRE OÙ ELLES FINISSENT : la plus rapide d'abord.
    for finished in asyncio.as_completed(tasks):

        # "await" veut dire : "attends le résultat de celle-ci".
        # Pendant cette attente, les autres Tasks continuent.
        delay = await finished

        # On ajoute le temps obtenu à la fin de la liste.
        delays.append(delay)

    # ÉTAPE 4 : renvoyer la liste, déjà triée.
    # Attention : ce "return" est HORS de la boucle "for"
    # (même indentation que "for"), sinon on s'arrêterait au 1er tour.
    return delays
