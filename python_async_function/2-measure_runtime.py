#!/usr/bin/env python3
"""
Ce module mesure combien de temps prend la fonction wait_n.

Rappel :
- wait_n(n, max_delay) lance n attentes au hasard EN MÊME TEMPS,
  puis renvoie la liste des temps d'attente (voir la tâche 1).
- Ici, on veut savoir combien de temps tout ça dure réellement,
  comme si on déclenchait un chronomètre.
"""

# On importe asyncio pour pouvoir lancer une coroutine
# depuis une fonction normale (voir plus bas, asyncio.run).
import asyncio

# On importe time : c'est le module qui sert de chronomètre.
import time

# On récupère la fonction "wait_n" écrite dans la tâche 1.
# Comme pour la tâche 1, on utilise __import__ car le nom
# du fichier commence par un chiffre.
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps total d'exécution de wait_n(n, max_delay)
    et renvoie le temps moyen par coroutine.

    Paramètres :
        n : le nombre de coroutines que wait_n va lancer.
        max_delay : le temps d'attente maximum, en secondes.

    Renvoie :
        Le temps total divisé par n, sous forme de float.
    """

    # ATTENTION : cette fonction est déclarée avec "def",
    # PAS avec "async def". C'est une fonction normale.
    # Elle ne peut donc pas utiliser "await".

    # ÉTAPE 1 : démarrer le chronomètre.
    # time.perf_counter() renvoie un nombre de secondes très précis.
    # La valeur seule ne veut rien dire : on s'en sert pour
    # calculer une DIFFÉRENCE entre deux moments.
    start: float = time.perf_counter()

    # ÉTAPE 2 : lancer wait_n et attendre qu'elle se termine.
    # Comme on est dans une fonction normale, on ne peut pas écrire
    # "await wait_n(...)". On utilise asyncio.run(), qui :
    #   - démarre le chef d'orchestre d'asyncio,
    #   - fait tourner la coroutine jusqu'au bout,
    #   - puis s'arrête.
    # On ne garde pas le résultat : seul le temps nous intéresse.
    asyncio.run(wait_n(n, max_delay))

    # ÉTAPE 3 : arrêter le chronomètre.
    # Temps écoulé = heure de fin - heure de départ.
    end: float = time.perf_counter()
    total_time: float = end - start

    # ÉTAPE 4 : renvoyer le temps moyen, comme demandé par le sujet.
    # Le "/" en Python donne toujours un float, même entre deux int.
    return total_time / n
