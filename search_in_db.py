from own_db_helpers import load_films


def search_for_film(keyword, films):
    keyword_films = set()
    for film in films:
        if keyword.lower() in film['original_title'].lower():
            keyword_films.add(film['original_title'])
    return keyword_films


def main():
    path_to_db = input('Enter path to DataBase:')
    films = load_films(path_to_db)

    keyword = input('Enter film to search for:')
    keyword_films = search_for_film(keyword, films)
    for film in sorted(keyword_films):
        print(film)


if __name__ == '__main__':
    main()
