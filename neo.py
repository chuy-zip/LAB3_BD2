from connection import get_neo_driver
from search import search_user, search_movie
from genre_creator import creat_genre
from movie_creator import create_movie
from person_creator import create_person

driver = get_neo_driver()

#aqui voy a poner las llamadas a las funciones para hacer los nodos del inciso 4

try:
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

finally:
    driver.close()