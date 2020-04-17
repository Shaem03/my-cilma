import requests
import json


def searchMovies(search_input):
    movie_result = {"tmdb_rating": "NA"}
    try:
        api_key = "3aca899f8fe1c1ede4ec01d1acd5f0f4"
        poster_url = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
        search_movie = "https://api.themoviedb.org/3/search/movie?api_key=%s&query=%s" % (api_key, search_input)
        response = requests.get(url=search_movie)
        movie_details = json.loads(response.content)

        movie_respomse = movie_details['results'][0]
        if movie_respomse:
            movie_result = {
                'title': movie_respomse['title'],
                'poster_path': poster_url + movie_respomse['poster_path'],
                'overview': movie_respomse['overview'],
                'release_date': movie_respomse['release_date'],
                'tmdb_rating': movie_respomse['vote_average']
            }

        return movie_result
    except:
        return movie_result
