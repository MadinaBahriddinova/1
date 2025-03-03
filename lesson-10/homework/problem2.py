import requests
import random

def get_movie_recommendation(genre):
    api_key = "YOUR_TMDB_API_KEY"
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genre_response = requests.get(genre_url).json()
    
    genre_id = next((g["id"] for g in genre_response["genres"] if g["name"].lower() == genre.lower()), None)
    
    if not genre_id:
        print("Genre not found.")
        return
    
    movie_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    movie_response = requests.get(movie_url).json()
    
    if "results" in movie_response and movie_response["results"]:
        movie = random.choice(movie_response["results"])
        print(f"Recommended Movie: {movie['title']}")
        print(f"Overview: {movie['overview']}")
    else:
        print("No movies found for this genre.")

# Example Usage
get_movie_recommendation("Action")
