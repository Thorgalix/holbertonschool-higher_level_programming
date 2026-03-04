#!/usr/bin/python3
"""Fetch the first state from the database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion à MySQL avec : utilisateur, mot de passe, base de données.
    # sys.argv[1] = user, sys.argv[2] = password, sys.argv[3] = database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # On récupère tous les objets State, triés par id croissant.
    for state in (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
    ):
        # Affichage demandé par l'exercice : "id: name".
        print("{}: {}".format(state.id, state.name))

    session.close()
