#!/usr/bin/python3
"""Affiche toutes les villes triées par leur id"""
import sys
from model_state import Base, State
from model_city import City
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

    for city in session.query(City).order_by(City.id):
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()
