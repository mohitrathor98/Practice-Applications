'''
    User is able to add movies/ look entire collection/ search movie using movie name
    To quit the app: enter 'q' when asked

    App loads data from db.json file at start and at end dumps collection there
'''

import json

try:
    movie_collection = json.load(open('db.json'))
except Exception as e:
    print("Error while reading db.json file: " + e)


def run_menu():
    choice = input("\nCHOICES\n\na) Add movie\nb) Show collection\nc) Search movie by title\nq) quit\n\n")
    
    if choice not in ['a', 'b', 'c']:
        return False
    return choice


def add_new_movie():
    movie_name = input("Movie Name: ")
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
    print(movie_collection)

def search_by_title():
    search_word = input("Title to search: ")

    for movie in movie_collection:
        if movie['movie_name'] == search_word:
            print(movie)
            break
    else:
        print(f"\n{search_word} can't be found")


if __name__== "__main__":
    
    menu_choice = run_menu()
    while menu_choice:
        
        if menu_choice == 'a':
            add_new_movie()
        elif menu_choice == 'b':
            show_collection()
        else:
            search_by_title()

        menu_choice = run_menu()

    with open('db.json', 'w') as out:
        out.write(json.dumps(movie_collection))