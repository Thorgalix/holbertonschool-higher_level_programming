#!/usr/bin/python3
"""
Module task_02_requests

Exercice Holberton: Consuming and processing data from an API using Python.
"""

import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """
    Récupère tous les posts depuis l'API JSONPlaceholder et affiche les titres.

    Étapes :
    1. Envoie une requête GET à l'URL des posts.
    2. Affiche le status code de la réponse.
    3. Si la requête réussit (code 200), parse la réponse JSON.
    4. Affiche le titre de chaque post.

    Retour :
    Aucun (affiche directement dans la console).
    """
    response = requests.get(url)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """
    Récupère tous les posts depuis l'API JSONPlaceholder et les sauvegarde dans un CSV.

    Étapes :
    1. Envoie une requête GET à l'URL des posts.
    2. Si la requête réussit (code 200), parse la réponse JSON.
    3. Construit une liste de dictionnaires contenant les clés 'id', 'title', 'body'.
    4. Écrit cette liste dans un fichier 'posts.csv' avec les colonnes correspondantes.

    Fichier produit :
    - posts.csv : colonnes 'id', 'title', 'body', une ligne par post.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        post_list = []
        for post in data:
            post_list.append({
                "id": post['id'],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(post_list)
