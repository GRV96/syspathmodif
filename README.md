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
