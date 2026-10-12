#!/usr/bin/env python3
"""
Ce module montre comment transformer une coroutine en "Task" (tâche).

Rappel :
- Une coroutine est une fonction "async def". L'appeler sans "await"
  la prépare, mais ne la démarre pas.
- Une Task (tâche) est une coroutine que l'on a CONFIÉE au chef
  d'orchestre d'asyncio : il la démarre dès qu'il peut, sans attendre
  qu'on écrive "await".
"""

# On importe asyncio : c'est lui qui sait créer des Tasks.
import asyncio

# On récupère la fonction "wait_random" écrite dans la tâche 0.
# Pour rappel, wait_random(max_delay) attend un temps au hasard
# entre 0 et max_delay secondes, puis renvoie ce temps.
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une Task qui exécute wait_random(max_delay) et la renvoie.

    Paramètres :
        max_delay : le temps d'attente maximum, en secondes.

    Renvoie :
        Un objet asyncio.Task qui fait tourner wait_random.
    """

    # ATTENTION : cette fonction est déclarée avec "def",
    # PAS avec "async def", comme le demande le sujet.
    # Elle ne fait que CRÉER la tâche, elle n'attend rien.

    # ÉTAPE 1 : préparer la coroutine (rien ne démarre encore).
    coroutine = wait_random(max_delay)

    # ÉTAPE 2 : confier la coroutine au chef d'orchestre.
    # asyncio.create_task() emballe la coroutine dans une Task
    # et la programme pour qu'elle démarre dès que possible.
    # Important : create_task ne marche que si asyncio tourne déjà.
    # C'est le cas ici, car le fichier de test appelle notre
    # fonction depuis une coroutine lancée avec asyncio.run().
    task: asyncio.Task = asyncio.create_task(coroutine)

    # ÉTAPE 3 : renvoyer la tâche.
    # Celui qui la reçoit pourra plus tard écrire "await task"
    # pour attendre son résultat.
    return task
