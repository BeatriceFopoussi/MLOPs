# # § ====================  Test Function to query the database tables" ====================

from database import SessionLocal
from API.query_helpers import *

db = SessionLocal()
# --- Test get_movie ---

movie = get_movie(db, movie_id=1)
print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")
db.close()


# %%
# Tester la récupération de films
#movies = query_helper.get_movies(db, limit=5, genre="Comedy")

#for movie in movies:
    #print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
# Fermer la session
db.close()