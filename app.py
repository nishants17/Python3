# Incomplete app!
from numpy.core.defchararray import title

# Providing the user with the available options
menu_prompt = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

# print(menu_prompt)

# This list will be the movie database for the user
movies = []  # User movie database


# User input Function
def user_input():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    budget = input("Enter the movie budget: ")
    actor = input("Enter the movie actor's name: ")
    return title, director, year, budget, actor  # Returns a tuple with the following elements present


# Add movie function
def add_movie():  # Input parameters from the user_input function appended to the existing list of movies
    add = [user_input()]  # This contains a tuple of user inputs
    movies.append({
        'title': add[0][0],  # This is the first user input in the tuple and so on
        'director': add[0][1],
        'year': add[0][2],
        'budget': add[0][3],
        'actor': add[0][4]
    })
    # print(movies)


# List movie function
def list_movies(m):  # List the user's present movie library
    print("Here is the list of all the movies present in your collection")
    print(m)


# Find movie function
def find_movie_by_title(movie_title):  # Find the movie by the user's title input
    for movie in movies:
        print(movie)
        print(type(movie))
        if movie['title'] == movie_title:
            # print(movie)
            print(movie)
            return movie
        else:
            continue
    print("This movie in not present in your library. Do you wish to add it now?")
    add_now()


def add_now():  # This function is triggered if the movie is not present in your library
    response = input("Enter y or n: ")
    if response == 'y':
        add_movie()
        print("Movie added successfully to your collection!")
        user_menu()
    elif response == 'n':
        user_menu()
    else:
        print("Invalid input. Please try again with correct input y or n")
        add_now()


# And another function here for the user menu
def user_menu():
    selection = input(menu_prompt)  # Providing users with the available options to choose from
    # print(selection)
    while selection != "q":  # Exit from the user menu
        # print(selection)
        if selection == "a":  # Add a movie to our existing collection
            add_movie()
            print("Movie added successfully to your collection!")
            user_menu()
        elif selection == "l":  # List all the movies present in our list
            list_movies(movies)
            print("I hope you are proud of this list :)")
            # selection = input(menu_prompt)
            user_menu()
        elif selection == "f":  # Find a movie from our existing collection by title
            print(selection)
            find_movie = input("Enter the movie title you want to find: ")
            # print(selection)  # Testing why the q user input is bringing us in this part of the conditional loop
            movie_found = find_movie_by_title(find_movie)
            if movie_found:  # Only print if the movie is found else do nothing
                print(f"{movie_found['title']} is present in your collection")
                user_menu()
            else:
                pass
            # user_menu()
        else:
            print('Unknown command. Please try again.')
            # selection = input(menu_prompt)
    print("You have now successfully exited the user menu")
    exit()


# Remember to run the user menu function at the end!
user_menu()
