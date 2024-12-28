# syspathmodif

## FRANÇAIS

Cette bibliothèque offre des manières concises de modifier la liste `sys.path`.
L'utilisateur ne devrait pas avoir besoin d'interagir directement avec cette
liste.

### Contenu

Les fonctions de `syspathmodif` prennent un chemin de type `str` ou
`pathlib.Path` comme argument.
Elles convertissent les arguments de type `pathlib.Path` en `str` puisque
`sys.path` n'est censée contenir que des chaînes de caractères.

* `sp_append` ajoute le chemin donné à la fin de `sys.path`.
* `sp_contains` indique si `sys.path` contient le chemin donné.
* `sp_remove` enlève le chemin donné de `sys.path`.

Dès son instanciation, la classe `SysPathBundle` contient plusieurs chemins et
les ajoute à `sys.path`. Quand on vide (*clear*) une instance, elle efface son
contenu et l'enlève de `sys.path`. Ainsi, cette classe facilite l'ajout et le
retrait d'un groupe de chemins.

Pour plus d'informations, consultez la documentation des fonctions et les démos
dans le dépôt de code source.

### Dépendances

Installez les dépendances de `syspathmodif` avant de l'utiliser.
```
pip install -r requirements.txt
```

Cette commande installe les dépendances de développement en plus des
dépendances ordinaires.
```
pip install -r requirements-dev.txt
```

### Démos

Les scripts dans le dossier `demos` montrent comment `syspathmodif` permet
d'importer un paquet qui est indisponible tant qu'on n'a pas ajouté son chemin
à `sys.path`. Les deux démos dépendent du paquet `demo_package`.

À l'aide de la classe `SysPathBundle`, `demo_bundle.py` ajoute la racine du
dépôt et `demo_package` à `sys.path`. La suppression de l'instance de
`SysPathBundle` annule cette modification.
```
python demos/demo_bundle.py
```

À l'aide des fonctions `sp_append` et `sp_remove`, `demo_functions.py` ajoute
la racine du dépôt à `sys.path` puis l'en enlève.
```
python demos/demo_functions.py
```

### Tests automatiques

Cette commande exécute les tests automatiques.
```
pytest tests
```

## ENGLISH

This library offers concise manners to modify list `sys.path`.
The user should not need to directly interact with that list.

### Content

The functions in `syspathmodif` take a path of type `str` or `pathlib.Path`
as an argument.
They convert arguments of type `pathlib.Path` to `str` since `sys.path` is
supposed to contain only character strings.

* `sp_append` appends the given path to the end of `sys.path`.
* `sp_contains` indicates whether `sys.path` contains the given path.
* `sp_remove` removes the given path from `sys.path`.

Upon instantiation, class `SysPathBundle` stores several paths and adds them to
`sys.path`. When a bundle is cleared, it erases its content and removes it from
`sys.path`. Thus, this class facilitates adding and removing a group of paths.

For more information, consult the functions' documentation and the demos in the
source code repository.

### Dependencies

Install the dependencies before using `syspathmodif`.
```
pip install -r requirements.txt
```

This command installs the development dependencies in addition to the ordinary
dependencies.
```
pip install -r requirements-dev.txt
```

### Demos

The scripts in directory `demos` show how `syspathmodif` allows to import a
package unavailable unless its path is added to `sys.path`. Both demos depend
on `demo_package`.

With class `SysPathBundle`, `demo_bundle.py` adds the repository's root and
`demo_package` to `sys.path`. The deletion of the `SysPathBundle` instance
undoes this modification.
```
python demos/demo_bundle.py
```

With functions `sp_append` and `sp_remove`, `demo_functions.py` adds the
repository's root to `sys.path` then removes it.
```
python demos/demo_functions.py
```

### Automated Tests

This command executes the automated tests.
```
pytest tests
```
