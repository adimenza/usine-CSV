# Export CSV

Exécutez cet exemple depuis la racine du dépôt pour exporter une seule ligne de données.

```python
from export import export

print(export([[7, "Dupont, Alice"]]), end="")
```

Le CSV obtenu contient un en-tête et place le nom entre guillemets parce qu’il contient une virgule.

```csv
id,name
7,"Dupont, Alice"
```
