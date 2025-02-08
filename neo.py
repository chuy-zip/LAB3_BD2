from connection import get_neo_driver
from search import search_user, search_movie

driver = get_neo_driver()

try:
    search_user(driver, "Clinton Spencer")
    search_movie(driver, "Apollo 13")
    
finally:
    driver.close()