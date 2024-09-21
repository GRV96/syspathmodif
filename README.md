# syspathmodif

## FRANÇAIS

Cette bibliothèque aide à modifier le contenu de la liste `sys.path`.

### Fonctions

Les fonctions de `syspathmodif` prennent un chemin de type `str` ou
`pathlib.Path` comme argument.
Elles convertissent les arguments de type `pathlib.Path` en `str` puisque
`sys.path` n'est censée contenir que des chaînes de caractères.

* `sp_append` ajoute le chemin donné à la fin de `sys.path`.
* `sp_contains` indique si `sys.path` contient le chemin donné.
* `sp_remove` enlève le chemin donné de `sys.path`.

### Démo

Le script dans le dossier `demo` montre comment `syspathmodif` permet
d'importer un paquet indisponible sans l'ajout d'un chemin à `sys.path`.
Il dépend du paquet `demo_package`.
Lancez la démo avec la commande suivante.

```
python demo/demo.py
```

### Tests automatiques

Installez `pytest`.
```
pip install pytest
```

Exécutez les tests.
```
pytest tests/test_syspathmodif.py
```

## ENGLISH

This library helps to modify the content of list `sys.path`.

### Functions

The functions in `syspathmodif` take a path of type `str` or `pathlib.Path`
as an argument.
They convert arguments of type `pathlib.Path` to `str` since `sys.path` is
supposed to contain only character strings.

* `sp_append` appends the given path to the end of `sys.path`.
* `sp_contains` indicates whether `sys.path` contains the given path.
* `sp_remove` removes the given path from `sys.path`.

### Demo

The script in directory `demo` shows how `syspathmodif` allows to import a
package unavailable without adding a path to `sys.path`.
It depends on `demo_package`.
Run the demo with the following command.

```
python demo/demo.py
```

### Automated Tests

Install `pytest`.
```
pip install pytest
```

Run the tests.
```
pytest tests/test_syspathmodif.py
```
