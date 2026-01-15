#!/usr/bin/python3
import marshal, types

if __name__ == "__main__":
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)   # ignorer l’entête du .pyc (magic number + timestamp)
        code = marshal.load(f)   # charger le code compilé
    module = types.ModuleType("hidden_4")  # créer un module vide
    exec(code, module.__dict__)            # exécuter le code dans ce module

    # récupérer les noms
    names = [n for n in dir(module) if not n.startswith("__")]
    for name in sorted(names):
        print(name)
