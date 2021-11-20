'''
    User is able to add movies/ look entire collection/ search movie using movie name
    To quit the app: enter 'q' when asked

    App loads data from db.json file at start and at end dumps collection there
'''

import json

try:
    movie_collection = json.load(open('Movie-Collection-Python/db.json'))
except Exception as e:
    print("\nError while reading db.json file: " + e)


def run_menu():
    print("\n======================================")
    print("CHOICES")
    print("======================================")
    choice = input("\n\na) Add movie\nb) Show collection\nc) Search movie by title\nq) quit\n\n")
    
    if choice not in ['a', 'b', 'c']:
        return False
    return choice


def add_new_movie():
    movie_name = input("\nMovie Name: ")
    director_name = input("Director Name: ")
    release_year = input("Release Year: ")
    available_platform = input("Available Platform: ")

    movie_collection.append(
        {
            'movie_name': movie_name,
            'director_name': director_name,
            'release_year': release_year,
            'available_platform': available_platform
        }
    )


def show_collection():
    print("\n", json.dumps(movie_collection, indent=4))


def search_by_title():
    search_word = input("\nTitle to search: ")

    for movie in movie_collection:
        if movie['movie_name'].lower() == search_word.lower():
            print("\n", json.dumps(movie, indent=4))
            break
    else:
        print(f"\n{search_word} can't be found")



choices = {
    'a' : add_new_movie,
    'b' : show_collection,
    'c' : search_by_title
}

if __name__== "__main__":
    
    menu_choice = run_menu()
    while menu_choice:
        
        if menu_choice in choices:
            choices[menu_choice]()

        menu_choice = run_menu()

    with open('Movie-Collection-Python/db.json', 'w') as out:
        out.write(json.dumps(movie_collection))