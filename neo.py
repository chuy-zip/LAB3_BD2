from connection import get_neo_driver
from search import search_user, search_movie
from genre_creator import create_genre
from movie_creator import create_movie
from person_creator import create_person
from user_creator import create_user
from relation_creator import create_relation

driver = get_neo_driver()


try:

    #para el ejercicio 2, dice que cada user debe tener minimo 2 relaciones de rate. 
    # Entonces voy a poner 3 nodos de pelicula
    create_movie(driver, {
        "name": "The Matrix",
        "movield": 133093,
        "year": 1999,
        "plot": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."
    })

    create_movie(driver, {
        "name": "Interstellar",
        "movield": 816692,
        "year": 2014,
        "plot": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
    })

    create_movie(driver, {
        "name": "The Dark Knight",
        "movield": 468569,
        "year": 2008,
        "plot": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham."
    })
    
    #aqui voy a poner las llamadas a las funciones para hacer los nodos del inciso 4 (falta users y creación de relaciones)
    create_person(driver,['Person','Actor','Director'], {
        "name": "John Doe", 
        "imdbid": 123456, 
        "born": "1980-05-15", 
        "died": "None", 
        "bornin": "New York, USA",
        "url": "http://example.com/johndoe", 
        "bio": "An accomplished actor known for versatile roles.", 
        "poster": "http://example.com/poster/johndoe.jpg"})
    
    create_person(driver, ['Person', 'Actor'], {
        "name": "Alice Johnson",
        "imdbid": 789012,
        "born": "1992-08-22",
        "died": "None",
        "bornin": "Los Angeles, USA",
        "url": "http://example.com/alicejohnson",
        "bio": "A rising star in independent films.",
        "poster": "http://example.com/poster/alicejohnson.jpg"})
    
    create_person(driver, ['Person', 'Director'], {
        "name": "Michael Brown",
        "imdbid": 345678,
        "born": "1975-03-10",
        "died": "2020-12-25",
        "bornin": "London, UK",
        "url": "http://example.com/michaelbrown",
        "bio": "Award-winning director and screenwriter.",
        "poster": "http://example.com/poster/michaelbrown.jpg"})
    
    create_movie(driver, {
        "name": "Inception",
        "imdbId": 1375666,
        "released": "2010-07-16",
        "imdbRating": 8.8,
        "movield": 27205,
        "year": 2010,
        "runtime": 148,
        "countries": ["USA", "UK"],
        "imdbVotes": 2200000,
        "url": "http://www.imdb.com/title/tt1375666/",
        "revenue": 829895144,
        "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "poster": "http://example.com/poster/inception.jpg",
        "budget": 160000000,
        "languages": ["English", "Japanese", "French"]})
    
    create_genre(driver, "Action")

    create_user(driver, {"name": "Jorge", "userid": "1"})

    create_user(driver, {"name": "Mario", "userid": "2"})
    
    create_user(driver, {"name": "Dan", "useris": "3"})

    create_user(driver, {"name": "Ana", "userid": "4"})

    create_relation(driver, "User", "Dan", "Movie", "The Matrix", "RATED", {"rating": 4, "timeStamp": 60})

finally:
    driver.close()