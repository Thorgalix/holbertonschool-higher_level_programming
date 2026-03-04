#!/usr/bin/python3
"""Fetch all states from the database."""
# sys permet de lire les arguments passés dans le terminal.
import sys
# On importe le modèle State et la base ORM définis dans model_state.py.
from model_state import Base, State
# create_engine crée la connexion SQLAlchemy vers MySQL.
from sqlalchemy import create_engine
# sessionmaker sert à fabriquer des sessions (canal de communication ORM).
from sqlalchemy.orm import sessionmaker

# Ce bloc garantit que le code s'exécute seulement si on lance ce fichier.
if __name__ == "__main__":
    # Connexion à MySQL avec : utilisateur, mot de passe, base de données.
    # sys.argv[1] = user, sys.argv[2] = password, sys.argv[3] = database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # On crée une "fabrique" de sessions liée à cet engine.
    Session = sessionmaker(bind=engine)
    # On ouvre une session pour interroger la base via l'ORM.
    session = Session()

    # On récupère tous les objets State, triés par id croissant.
    for state in session.query(State).order_by(State.id):
        # Affichage demandé par l'exercice : "id: name".
        print("{}: {}".format(state.id, state.name))

    # Bonne pratique : fermer la session quand on a fini.
    session.close()
