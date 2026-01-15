#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = dir(module)
    filtername = []
    for name in names:
        if not name.startswith("__"):
            filtername.append(name)
    
    for name in sorted(filtername):
        print(name)
