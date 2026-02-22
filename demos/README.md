# Les démos

Les commandes doivent être lancées à partir de la racine du dépôt.

`demo1_individual_paths.py` ajoute la racine du dépôt à `sys.path` à l'aide de
la fonction `sp_prepend`. Après les importations, la démo annule cette
modification à l'aide de la fonction `sp_remove`.
```
python demos/demo1_individual_paths.py
```

`demo2_bundle.py` ajoute la racine du dépôt et le dossier `demo_package` à
`sys.path` à l'aide de la classe `SysPathBundle`. Après les importations, la
démo annule ces modifications en vidant l'instance de `SysPathBundle`.
```
python demos/demo2_bundle.py
```

`demo3_bundle_context.py` effectue la même tâche que `demo2_bundle.py` en
utilisant `SysPathBundle` comme gestionnaire de contexte.
```
python demos/demo3_bundle_context.py
```

`demo4_bundle_none_empty.py` imite une situation où ajouter des chemins de
dossier à `sys.path` est optionnel. L'utilisateur peut instancier
`SysPathBundle` avec le contenu de son choix.

Aide:
```
python demos\demo4_bundle_none_empty.py -h
```

Exemple d'exécution:
```
python demos\demo4_bundle_none_empty.py --paths . demo_package
```

`demo5_sm_contains_A.py` montre un cas où on peut importer un module sans
ajouter son chemin parent à `sys.path`. La démo vérifie la présence du module
dans `sys.modules` à l'aide de la fonction `sm_contains`.
```
python demos/demo5_sm_contains_A.py
```

`demo6_sm_contains_B.py` montre un autre usage de la fonction `sm_contains`.
```
python demos/demo6_sm_contains_B.py
```

`demo7_parent.py` ajoute la racine du dépôt à `sys.path` à l'aide de la
fonction `sp_prepend_parent`. Après les importations, la démo annule cette
modification à l'aide de la fonction `sp_remove`.
```
python demos/demo7_parent.py
```

`demo8_parent_bundle.py` met le chemin de la racine du dépôt dans une instance
de `SysPathBundle` à l'aide de la fonction `sp_prepend_parent_bundle`.
L'instance sert de gestionnaire de contexte.
```
python demos/demo8_parent_bundle.py
```

# Demos

The commands must be run from the repository's root.

`demo1_individual_paths.py` adds the repository's root to `sys.path` with
function `sp_prepend`. After the imports, the demo undoes this modification
with function `sp_remove`.
```
python demos/demo1_individual_paths.py
```

`demo2_bundle.py` adds the repository's root and `demo_package` to `sys.path`
with class `SysPathBundle`. After the imports, the demo undoes these
modifications by clearing the `SysPathBundle` instance.
```
python demos/demo2_bundle.py
```

`demo3_bundle_context.py` performs the same task as `demo2_bundle.py` by using
`SysPathBundle` as a context manager.
```
python demos/demo3_bundle_context.py
```

`demo4_bundle_none_empty.py` imitates a situation where prepending directory
paths to sys.path is optional. The user can instantiate a `SysPathBundle` with
the content of their choice.

Help:
```
python demos\demo4_bundle_none_empty.py -h
```

Execution example:
```
python demos\demo4_bundle_none_empty.py --paths . demo_package
```

`demo5_sm_contains_A.py` shows a case where a module can be imported without its
parent path being added to `sys.path`. The demo verifies the module's presence
in `sys.modules` with function `sm_contains`.
```
python demos/demo5_sm_contains_A.py
```

`demo6_sm_contains_B.py` shows another use of function `sm_contains`.
```
python demos/demo6_sm_contains_B.py
```

`demo7_parent.py` adds the repository's root to `sys.path` with function
`sp_prepend_parent`. After the imports, the demo undoes this modification with
function `sp_remove`.
```
python demos/demo7_parent.py
```

`demo8_parent_bundle.py` puts the path to the repository's root in a
`SysPathBundle` instance with function `sp_prepend_parent_bundle`. The bundle
is used as a context manager.
```
python demos/demo8_parent_bundle.py
```
