# Python - Async

Projet Holberton School (`holbertonschool-web_back_end/python_async_function`) :
introduction à la programmation asynchrone en Python avec `async` / `await` et le
module `asyncio`.

Ce README sert aussi de **fiche de révision** : il reprend, dans l'ordre, tout ce
que j'ai appris pendant le projet.

---

## Ce que j'ai appris

### 1. Les annotations de type

Une annotation est une étiquette qui indique le type attendu d'une valeur :
`int` (entier), `float` (nombre à virgule), `str` (texte).

- Paramètre : `nom: type`
- Valeur renvoyée : `-> type`, placé **avant** les deux-points de fin
- Les deux-points `:` sont **toujours le dernier caractère** de la ligne `def`

```python
def repeter(mot: str, fois: int) -> str:
```

Avec une valeur par défaut, l'ordre est `nom: type = valeur`. Attention au style :
sans annotation on écrit `n=10` (sans espaces), mais avec une annotation,
`pycodestyle` exige **des espaces** autour du `=` : `n: int = 10`.

```python
def puissance(base: float, exposant: int = 2) -> float:
```

Python ne fait **pas** respecter les annotations à l'exécution : elles documentent
le code et aident les outils de vérification. Holberton les exige partout.

`int`, `float` et `str` ne demandent aucun import. Pour annoter une **liste** en
Python 3.8, il faudra importer depuis le module `typing` (tâche 1).

### 2. Le module `random`

```python
import random

note = random.uniform(0, 20)
```

`random.uniform(a, b)` renvoie un nombre à virgule au hasard entre `a` et `b`,
**bornes incluses**. Il est donc inutile d'écrire `0.01` ou `19.99` : on met
directement les limites demandées.

Chaque appel donne un **nouveau** nombre. Pour réutiliser la même valeur, on la
tire **une seule fois** et on la range dans une variable.

### 3. Synchrone ou asynchrone

**Synchrone** (le fonctionnement par défaut) : une instruction après l'autre.
Une attente est **bloquante**, car pendant ce temps le programme ne fait rien
d'autre. Les durées d'attente **s'additionnent**.

> Attentes de 2 s, 3 s et 1 s en synchrone : 2 + 3 + 1 = **6 s**.

**Asynchrone** : quand une tâche attend, on la met de côté et on avance sur une
autre. L'ordinateur ne calcule pas deux choses à la fois, il **profite des temps
morts**. Des attentes indépendantes lancées ensemble **se superposent** : le
total correspond environ à **l'attente la plus longue**.

> Les mêmes attentes en asynchrone : environ **3 s**.

Image à retenir : en cuisine, on lance l'eau des pâtes et on coupe les légumes
**pendant** qu'elle chauffe, au lieu de rester planté devant la casserole.

### 4. Les coroutines : `async def`

```python
async def chauffer_eau(minutes: int) -> str:
    """Simule la chauffe de l'eau et annonce qu'elle bout."""
    return "L'eau bout"
```

Une fonction déclarée avec `async def` est une **coroutine** : une fonction
capable de se mettre en pause et de reprendre plus tard. Les annotations
s'écrivent comme d'habitude ; `-> type` indique ce qu'elle renvoie à la fin.

**Piège principal** : appeler une coroutine **ne l'exécute pas**.

```python
print(chauffer_eau(5))
```

Ce code n'affiche pas `L'eau bout`, mais une description du type
`<coroutine object chauffer_eau at 0x...>`, suivie d'un avertissement
`RuntimeWarning: coroutine 'chauffer_eau' was never awaited`. L'appel fabrique
seulement une « recette », sans la cuisiner.

> Si je vois `was never awaited` : j'ai appelé une coroutine sans la faire exécuter.

### 5. Exécuter une coroutine : `asyncio.run`

Le gestionnaire qui fait tourner les coroutines s'appelle la **boucle
d'événements** (*event loop*). Elle décide quelle coroutine avance, laquelle est
en pause, et quand la reprendre.

```python
import asyncio

resultat = asyncio.run(chauffer_eau(5))
print(resultat)   # L'eau bout
```

`asyncio.run()` démarre la boucle, exécute la coroutine jusqu'au bout, **renvoie
sa valeur** puis ferme la boucle. On l'utilise une seule fois, au point de départ
du programme.

### 6. Attendre une coroutine : `await`

```python
async def preparer_repas() -> str:
    """Attend la chauffe de l'eau puis ajoute l'annonce du repas."""
    message = await chauffer_eau(2) + " - à table !"
    return message
```

`await coroutine()` signifie : « exécute cette coroutine, mets-moi en pause
jusqu'à ce qu'elle finisse, et donne-moi sa valeur ». Pendant cette pause, la
boucle d'événements fait avancer d'autres coroutines.

- `await` n'est autorisé **que dans un `async def`**
- `await` s'applique **avant** le `+` : on attend d'abord, puis on colle le texte
- En résumé : `asyncio.run` sert à **entrer** dans le monde asynchrone, et `await`
  sert à **circuler** à l'intérieur

### 7. Attendre sans bloquer : `asyncio.sleep`

```python
async def chauffer_eau(minutes: int) -> str:
    """Simule la chauffe de l'eau et annonce qu'elle bout."""
    await asyncio.sleep(minutes)
    return "L'eau bout"
```

- `time.sleep(n)` est **bloquant** : il fige toute la boucle d'événements. On
  ne l'utilise jamais dans une coroutine.
- `await asyncio.sleep(n)` met en pause **seulement la coroutine en cours**.
- `asyncio.sleep` est une coroutine : sans `await`, il **n'attend rien**.
- `asyncio.sleep` ne renvoie **pas** la durée attendue. Comme un minuteur de
  cuisine, il sonne mais ne dit pas combien de temps il a duré : c'est moi qui
  connais la durée, puisque c'est moi qui l'ai réglée.

**Ne pas écrire de valeur en dur** : `await asyncio.sleep(2)` ignore le paramètre
`minutes`. La durée doit venir du paramètre ou d'une variable.

### 8. Méthode : décortiquer un énoncé

Avant d'écrire du code, je transforme l'énoncé en **liste de contraintes**
vérifiables (oui / non) : nom, paramètres, types, valeur par défaut,
comportement, valeur renvoyée, fichier. La plupart des échecs aux tests viennent
d'un détail oublié, rarement d'une incompréhension.

Ensuite, je compare avec un code que j'ai déjà écrit et je découpe en petites
actions, une ligne à la fois.

---

## Tâche 0 : The basics of async

**Contraintes** : coroutine `wait_random`, paramètre `max_delay` entier avec
`10` par défaut, attente non bloquante d'un délai aléatoire (nombre à virgule)
entre 0 et `max_delay`, puis renvoi de ce délai (`float`). Modules utilisés :
`asyncio` et `random`.

**Construction en trois actions**, sur le modèle de `chauffer_eau` :

1. tirer le délai au hasard **une seule fois** et le ranger dans une variable ;
2. attendre ce délai, **avec `await`** ;
3. renvoyer **cette même variable**.

**Résultat** :

```bash
$ ./0-main.py
1.6302015129447323
2.8514987883414413
9.507852469301163
```

Chaque valeur est bien dans ses bornes (0–10, 0–5, 0–15).

**Erreurs que j'ai faites, et leur correction** :

- `await` oublié devant `asyncio.sleep` : le programme n'attend pas du tout ;
- résultat de `asyncio.sleep` stocké et renvoyé : il ne contient pas la durée,
  il faut renvoyer la variable du délai tiré.

---

## Bonnes habitudes

- **Relire les noms caractère par caractère** : `ramdom` au lieu de `random`
  provoque une `NameError`.
- **Vérifier ses calculs** : en tâche 2, une seconde d'écart fera échouer le test.
- **Comparer les sorties exactement** : un espace manquant suffit à faire échouer
  un test Holberton.
- **Laisser l'outil vérifier le style** : `pycodestyle fichier.py` n'affiche rien
  si tout est correct. Deux lignes vides entre deux fonctions.
- **Prédire avant de tester** : écrire sa prédiction, puis exécuter pour la
  confirmer ou la corriger.
- **Ne pas pousser ses brouillons** : vérifier `git status` avant `git add`.

Vocabulaire : *e.g.* (*exempli gratia*) = « par exemple » ; *i.e.* (*id est*) =
« c'est-à-dire ».

---

### Questions pour me tester

1. Pourquoi `print(chauffer_eau(5))` n'affiche-t-il pas `L'eau bout` ?
2. Quelle est la différence entre `asyncio.run` et `await` ?
3. Pourquoi ne jamais utiliser `time.sleep` dans une coroutine ?
4. Trois attentes de 4 s, 1 s et 2 s : quelle durée totale en synchrone, et en
   asynchrone ?
5. Que se passe-t-il si on appelle `random.uniform` deux fois dans `wait_random` ?

---
