import json
import urllib.parse
import urllib.request

from tmdb_helpers import get_user_api_key
from tmdb_helpers import make_tmdb_api_request


def load_films(user_api_key, films_amount=1000):
    films = []
    for film_id in range(films_amount):
        try:
            films.append(
                make_tmdb_api_request(method=f'/movie/{film_id}',
                                      api_key=user_api_key))
        except urllib.error.HTTPError as err:
            if err.code == 404:  # if no film on this id
                continue
            else:
                raise
        finally:
            print(f'{film_id * 100 / films_amount} percent complete')
    return films


def main():
    user_api_key = get_user_api_key()
    if not user_api_key:
        print('Invalid api key')
        raise SystemExit
    films_amount = 1000
    print('please, wait, this operation may take smth like 15-20 minutes')
    films = load_films(user_api_key, films_amount)
    with open('MyFilmDB.json', mode='w', encoding='utf-8') as films_file:
        json.dump(films, films_file)


if __name__ == '__main__':
    main()
