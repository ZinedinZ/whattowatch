import requests
import json

class FindMovie:
    def __init__(self):
        self.genres = {28: 'Action', 12: 'Adventure', 16: 'Animation', 35: 'Comedy', 80: 'Crime', 99: 'Documentary',
                       18: 'Drama', 10751: 'Family', 14: 'Fantasy', 36: 'History', 27: 'Horror', 10402: 'Music',
                       9648: 'Mystery', 10749: 'Romance', 878: 'Science Fiction', 10770: 'TV Movie', 53: 'Thriller',
                       10752: 'War', 37: 'Western'
                       }
        self.api_key= "d0e2f5b7d0c7c63fa48e05b4b6a120f9"
        self.account_id = "20711802"
        self.headers = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMGUyZjViN2QwYzdjNjNmYTQ4ZTA1YjRiNmExMjBmOSIsInN1YiI6IjY1NTY4MTIyNjdiNjEzNDVjY2FmNmM3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.sfogkJvuy-o4dfcInhIcTT5oh5uoAATfuG70gdX2fPM",
                        "language": "en-US",
                        "page": "1",
                        "with_genres": "27"
                        }

    def find_genres(self):
        user = input("What Movie genres you want? ").capitalize()
        genre = next((k for k, v in self.genres.items() if v == user), None)
        return genre

    def fin_movie(self, genre):
        self.url= f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre}"
        request = requests.get(self.url, headers=self.headers)
        data = json.loads(request.text)
        for movie in data["results"]:
            print(movie["title"])
