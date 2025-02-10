from connection import get_neo_driver
from search import search_user, search_movie
from genre_creator import create_genre
from movie_creator import create_movie
from person_creator import create_person
from user_creator import create_user
from relationship_creator import create_relationship

import datetime

driver = get_neo_driver()


def graph_exercise_2():
    try:
        #para el ejercicio 2, dice que cada user debe tener minimo 2 relaciones de rate. 
        # Entonces voy a poner 3 nodos de pelicula
        create_movie(driver, {
            "title": "The Matrix",
            "movield": 133093,
            "year": 1999,
            "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."
        })

        create_movie(driver, {
            "title": "Interstellar",
            "movield": 816692,
            "year": 2014,
            "plot": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
        })

        create_movie(driver, {
            "title": "The Dark Knight",
            "movield": 468569,
            "year": 2008,
            "plot": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."
        })

        # 5 usuarios
        create_user(driver, {"name": "Jorge", "userid": "1"})

        create_user(driver, {"name": "Mario", "userid": "2"})
        
        create_user(driver, {"name": "Dan", "userid": "3"})

        create_user(driver, {"name": "Ana", "userid": "4"})

        create_user(driver, {"name": "Chuy", "userid": "5"})

        # cada usuario califica minimo 2 peliculas
        create_relationship(driver,"RATED", {"rating":5,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Jorge"}}, {"labels": "Movie", "attributes": {"title": "The Matrix"}})
        create_relationship(driver,"RATED", {"rating":4,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Jorge"}}, {"labels": "Movie", "attributes": {"title": "Interstellar"}})

        create_relationship(driver,"RATED", {"rating":3,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Mario"}}, {"labels": "Movie", "attributes": {"title": "The Matrix"}})
        create_relationship(driver,"RATED", {"rating":5,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Mario"}}, {"labels": "Movie", "attributes": {"title": "The Dark Knight"}})
        
        create_relationship(driver,"RATED", {"rating":5,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Dan"}}, {"labels": "Movie", "attributes": {"title": "The Matrix"}})
        create_relationship(driver,"RATED", {"rating":4,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Dan"}}, {"labels": "Movie", "attributes": {"title": "Interstellar"}})

        create_relationship(driver,"RATED", {"rating":3,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Ana"}}, {"labels": "Movie", "attributes": {"title": "Interstellar"}})
        create_relationship(driver,"RATED", {"rating":5,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Ana"}}, {"labels": "Movie", "attributes": {"title": "The Dark Knight"}})
        
        create_relationship(driver,"RATED", {"rating":4,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Chuy"}}, {"labels": "Movie", "attributes": {"title": "The Matrix"}})
        create_relationship(driver,"RATED", {"rating":5,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Chuy"}}, {"labels": "Movie", "attributes": {"title": "The Dark Knight"}})

    finally:
        driver.close()

def graph_exersice_4():
    try:
        #aqui voy a poner las llamadas a las funciones para hacer los nodos del inciso 4 (falta users y creación de relaciones)
        #PERSON ACTOR DEIRECTOR
        create_person(driver, ['Person', 'Actor', 'Director'], {
            "name": "Mel Gibson",
            "imdbid": 128,
            "born": "1956-01-03",
            "died": "None",  # Sigue vivo
            "bornin": "Peekskill, New York, USA",
            "url": "https://www.imdb.com/name/nm0000154/",
            "bio": "Academy Award-winning actor and director known for his roles in Braveheart, Lethal Weapon, and directing films like Hacksaw Ridge.",
            "poster": "https://image.tmdb.org/t/p/w500/cFJ7ojI2vvruCqz5Vzrk4pM0G9c.jpg"
        })
        
        # PERSON ACTOR
        create_person(driver, ['Person', 'Actor'], {
            "name": "Leonardo DiCaprio",
            "imdbid": 6194,
            "born": "1974-11-11",
            "died": "None",  # Sigue vivo
            "bornin": "Los Angeles, California, USA",
            "url": "https://www.imdb.com/name/nm0000138/",
            "bio": "Academy Award-winning actor known for his performances in Titanic, The Revenant, and Inception.",
            "poster": "https://image.tmdb.org/t/p/w500/wo2hJpn04vbtmh0B9utCFdsQhxM.jpg"
        })
        
        #PERSON DIRECTOR
        create_person(driver, ['Person', 'Director'], {
            "name": "Christopher Nolan",
            "imdbid": 1204,
            "born": "1970-07-30",
            "died": "None",  # Sigue vivo
            "bornin": "London, England, UK",
            "url": "https://www.imdb.com/name/nm0634240/",
            "bio": "Acclaimed filmmaker known for his cerebral, often nonlinear storytelling.",
            "poster": "https://image.tmdb.org/t/p/w500/oPUwkfF64r6uCVLrH6NcTKff5No.jpg"
        })
        
        create_movie(driver, {
            "title": "Inception",
            "tmdbId": 27205,
            "released": "2010-07-16",
            "imdbRating": 8.8,
            "movield": 1375666,
            "year": 2010,
            "imdbId": "tt1375666",
            "runtime": 148,
            "countries": ["USA", "UK"],
            "imdbVotes": 2391230,
            "url": "https://www.imdb.com/title/tt1375666/",
            "revenue": 836848102,
            "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
            "poster": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
            "budget": 160000000,
            "languages": ["English", "Japanese", "French"]
        })
        
        create_genre(driver, "Action")

        create_user(driver, {"name": "Eunice", "userid": "6"})

        #relaciones
        #movie-genre
        create_relationship(driver,"IN_GENRE", {},{"labels": "Movie", "attributes": {"title": "Inception"}}, {"labels": "Genre", "attributes": {"name": "Action"}})

        #actor director - movie
        create_relationship(driver,"ACTED_IN", {"role":"William Wallace"},{"labels": "Actor", "attributes": {"name": "Mel Gibson"}}, {"labels": "Movie", "attributes": {"title": "Inception"}})
        create_relationship(driver,"DIRECTED", {"role":"Director"}, {"labels": "Director", "attributes": {"name": "Mel Gibson"}}, {"labels": "Movie", "attributes": {"title": "Inception"}})
        
        #actor - movie
        create_relationship(driver,"ACTED_IN", {"role":"Dom Cobb"},{"labels": "Actor", "attributes": {"name": "Leonardo DiCaprio"}}, {"labels": "Movie", "attributes": {"title": "Inception"}})

        #director - movie
        create_relationship(driver,"DIRECTED", {"role":"Director"}, {"labels": "Director", "attributes": {"name": "Christopher Nolan"}}, {"labels": "Movie", "attributes": {"title": "Inception"}})

        #user - movie
        create_relationship(driver,"RATED", {"rating":5,"timeStamp":datetime.datetime.now()},{"labels": "User", "attributes": {"name": "Eunice"}}, {"labels": "Movie", "attributes": {"title": "Inception"}})

    finally:
        driver.close()

