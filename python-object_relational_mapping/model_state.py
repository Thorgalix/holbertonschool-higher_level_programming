#!/usr/bin/python3
"""Module that defines a State class and declarative Base."""
# On importe les types de colonnes SQL dont on a besoin.
from sqlalchemy import Column, Integer, String
# Cet utilitaire crée une classe de base pour les modèles ORM.
from sqlalchemy.ext.declarative import declarative_base

# Base servira de "racine" à toutes les classes qui représentent des tables.
Base = declarative_base()


class State(Base):
    """State class that links to the states table."""
    # __tablename__ indique le nom exact de la table dans MySQL.
    __tablename__ = 'states'

    # Colonne id : entier, clé primaire, obligatoire.
    id = Column(Integer, primary_key=True, nullable=False)

    # Colonne name : texte (128 caractères max), obligatoire.
    name = Column(String(128), nullable=False)
