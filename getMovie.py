import requests
import json


def searchMovies(search_input):
    movie_result = {"overview": "NA"}
    try:
        api_key = "3aca899f8fe1c1ede4ec01d1acd5f0f4"
        search_movie = "https://api.themoviedb.org/3/search/movie?api_key=%s&query=%s" % (api_key, search_input)
        response = requests.get(url=search_movie)
        movie_details = json.loads(response.content)

        movie_respomse = movie_details['results'][0]
        if movie_respomse:
            movie_result = {
                'overview': movie_respomse['overview'],
            }

        return movie_result
    except:
        return movie_result
