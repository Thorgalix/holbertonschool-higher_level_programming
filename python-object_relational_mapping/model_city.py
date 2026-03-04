#!/usr/bin/python3
"""Module qui définit une classe City
qui hérite de la même Base que model_state."""
# On importe les types de colonnes SQL dont on a besoin.
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """City class that links to the states table."""
    # __tablename__ indique le nom exact de la table dans MySQL.
    __tablename__ = 'cities'

    # Colonne id : entier, clé primaire, obligatoire.
    id = Column(Integer, primary_key=True, nullable=False)

    # Colonne name : texte (128 caractères max), obligatoire.
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State")
