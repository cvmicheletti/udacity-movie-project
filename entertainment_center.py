#! /usr/bin/python2
# entertainment_center.py

import fresh_tomatoes
import media

""" This module is the main entry point into the MovieWebsite Project.  It
        constructs the Movie class instances needed to feed the fresh_tomatoes
        module. """

the_matrix = media.Movie("The Matrix", 136, "Andy and Lana Wachowski", 1999,
    "Neo, a computer hacker, finds his path is to be the one!",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/RATED_R.svg/46px-RATED_R.svg.png",
    "http://www.impawards.com/1999/posters/matrix_ver1.jpg",
    "https://www.youtube.com/watch?v=_Ls19O-9p3s")

contact = media.Movie("Contact", 150, "Carl Sagan", 1997,
    "Ellie Arraway finds an alien signal and travels to meet her deceased dad on a beach!",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/RATED_PG.svg/76px-RATED_PG.svg.png",
    "http://www.impawards.com/1997/posters/contact_ver2.jpg",
    "https://www.youtube.com/watch?v=SRoj3jK37Vc")

city_of_angels = media.Movie("City of Angels", 114, "Dana Stevens", 1998,
    "An angel named Seth is seen by Maggie, a heart surgeon, and falls in love and decides to become human",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/RATED_PG-13.svg/142px-RATED_PG-13.svg.png",
    "http://www.impawards.com/1998/posters/city_of_angels.jpg",
    "https://www.youtube.com/watch?v=wCrcDidiGJs")

blues_brothers = media.Movie("The Blues Brothers", 133, "John Landis", 1980,
    "Jake and Elwood Blues on a mission from God to save their orphanage!",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/RATED_R.svg/46px-RATED_R.svg.png",
    "http://www.impawards.com/1980/posters/blues_brothers_ver1.jpg",
    "https://www.youtube.com/watch?v=A-xtJYIwfYo")

fifth_element = media.Movie("The Fifth Element", 113, "Luc Besson", 1997,
    "Soldier turned taxi driver Corbin Dalas must save the world and his love Lilu",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/RATED_PG-13.svg/142px-RATED_PG-13.svg.png",
    "http://www.impawards.com/1997/posters/fifth_element_ver5.jpg",
    "https://www.youtube.com/watch?v=fQ9RqgcR24g")

holy_grail = media.Movie("Monty Python and the Holy Grail", 91, "Monty Python", 1975,
    "A twisted Arthurian quest for the grail that boggles the mind!",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/RATED_PG.svg/76px-RATED_PG.svg.png",
    "http://www.impawards.com/1975/posters/monty_python_and_the_holy_grail_ver1.jpg",
    "https://www.youtube.com/watch?v=hKNDml12Big")

bring_dead = media.Movie("Bringing Out the Dead", 121, "Joe Connelly", 1999,
    "NYC EMS Paramedic is haunted by dead patients and his PTSD and psycho partners.",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/RATED_R.svg/46px-RATED_R.svg.png",
    "http://www.impawards.com/1999/posters/bringing_out_the_dead.jpg",
    "https://www.youtube.com/watch?v=8TMg9WlKgsU")

# List passed into the fresh_tomatoes module method open_movies_page()
movies = [blues_brothers, bring_dead, city_of_angels, contact, fifth_element, the_matrix, holy_grail]

# Call into fresh_tomatoes to create the html file.
fresh_tomatoes.open_movies_page(movies)