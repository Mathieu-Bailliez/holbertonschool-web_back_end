#!/usr/bin/env python3
"""
Module qui mesure le temps d'exécution de tâches parallèles.

Ce module définit la coroutine measure_runtime qui lance quatre
async_comprehension en même temps avec asyncio.gather, puis
renvoie la durée totale de l'exécution en secondes.
"""

# asyncio.gather permet de lancer plusieurs coroutines en parallèle.
import asyncio

# time.perf_counter() est un chronomètre très précis, idéal pour
# mesurer une durée.
import time

# Même astuce qu'avant : le nom du fichier commence par un chiffre,
# donc on passe par __import__ pour récupérer la fonction.
async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute 4 fois async_comprehension en parallèle et mesure la durée.

    Les quatre coroutines attendent en même temps, donc la durée
    totale renvoyée est d'environ 10 secondes et non 40.
    """
    # 1) On démarre le chronomètre.
    debut = time.perf_counter()

    # 2) On lance les 4 coroutines en même temps.
    #    - (async_comprehension() for _ in range(4)) crée 4 coroutines
    #    - l'étoile "*" les "déballe" pour les passer une par une à
    #      gather, comme si on écrivait :
    #      gather(async_comprehension(), async_comprehension(),
    #             async_comprehension(), async_comprehension())
    #    - "await" attend que les 4 soient TOUTES terminées.
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    # 3) On arrête le chronomètre : durée = heure de fin - heure de début.
    #    Le résultat est un float (des secondes, avec décimales).
    return time.perf_counter() - debut
