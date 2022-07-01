from collections import OrderedDict

from own_db_helpers import load_films


def find_user_film(keyword, films):
    for film in films:
        if keyword == film['original_title']:
            return film


def get_recommendation_films(compared_film, films, recommend_amount=8):
    params = {
        'belongs_to_collection': 1000,
        'original_language': 300,
        'budget': 100,
        'genres': 500
    }
    rating = {}
    for film in films:
        film_rate = 0
        for parameter in params:
            if film[parameter] == compared_film[parameter]:
                film_rate += params[parameter]
        rating[film['original_title']] = film_rate
    rating.pop(compared_film['original_title'], None)
    rating = OrderedDict(
        sorted(rating.items(), key=lambda t: t[1], reverse=True))
    final_recommendation = []
    for film in rating:
        if len(final_recommendation) > recommend_amount:
            break
        final_recommendation.append(film)
    return final_recommendation


def main():
    path = input('Enter path to DataBase:')
    films = load_films(path)
    if not films:
        raise FileNotFoundError("File not found, sorry...")
    keyword = input('Enter film to search for:')
    user_film = find_user_film(keyword, films)
    if not user_film:
        raise FileNotFoundError("No such film in FilmsDB")
    recommendation_films = get_recommendation_films(user_film, films)
    for film in sorted(recommendation_films):
        print(film)


if __name__ == '__main__':
    main()
