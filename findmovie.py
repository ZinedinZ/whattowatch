import requests
import json
import os


class FindMovie:
    def __init__(self):
        self.genres = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary',
                       18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music',
                       9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller',
                       10752: 'War', 37: 'Western'
                       }
        self.url = ""
        self.auth = os.environ["tmdb_auth"]
        self.headers = {
                        "accept": "application/json",
                        "Authorization": self.auth,
                        "language": "en-US",
                        "page": "1",
                        }

    def find_genres(self, data):
        # Takes name of the genre from user and return genre id
        genre = next((k for k, v in self.genres.items() if v == data), None)
        return genre

    def find_movie(self, genre):
        self.url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=" \
                  f"en-US&page=1&sort_by=popularity.desc&with_genres={genre}"

        # Call tmdb API to get list of movies
        request = requests.get(self.url, headers=self.headers)
        data = json.loads(request.text)
        return data["results"]
