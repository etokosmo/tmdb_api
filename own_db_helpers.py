import json
import os


def load_films(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as films_file:
        films = json.load(films_file)
        return films
