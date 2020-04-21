import json

import requests
from justwatch import JustWatch
from getTv import MyCilmaTv


class MyCilma:

    def movieResult(self):
        just_watch = JustWatch(country='IN')
        # input_string = "hachiko"
        match_result = {}

        results = just_watch.search_for_item(query=self)

        for val in results['items']:
            hotstar_url = "NA"
            netflix_url = "NA"
            prime_url = "NA"
            rt_rating = "NA"
            imdb_rating = "NA"
            tmdb_rating = "NA"
            movie_id = ""
            overview = "NA"
            language = "NA"

            for subs_url in val["offers"]:
                if subs_url["urls"]['standard_web']:
                    url_provider = subs_url["urls"]['standard_web']
                    if "hotstar" in url_provider:
                        hotstar_url = subs_url["urls"]['standard_web']
                    elif "netflix" in url_provider:
                        netflix_url = subs_url["urls"]['standard_web']
                    elif "primevideo" in url_provider:
                        prime_url = subs_url["urls"]['standard_web']

            for ratings in val['scoring']:
                if ratings['provider_type'] == "tmdb:id":
                    movie_id = ratings['value']
                if ratings['provider_type'] == "tomato:meter":
                    rt_rating = ratings['value']
                elif ratings['provider_type'] == "imdb:score":
                    imdb_rating = ratings['value']
                elif ratings['provider_type'] == "tmdb:score":
                    tmdb_rating = ratings['value']

            poster_url = "https://images.justwatch.com%ss592" % val['poster'][:-9],
            movie_data = "https://api.themoviedb.org/3/movie/%s?api_key=3aca899f8fe1c1ede4ec01d1acd5f0f4" % movie_id
            movie_result = requests.get(url=movie_data)

            genres = []
            if movie_result.status_code == 200:
                movie_overview = json.loads(movie_result.content.decode('utf-8'))
                language = movie_overview['original_language']
                overview = movie_overview['overview']
                for vals in movie_overview['genres']:
                    genres.append(vals['name'])
            else:
                tv_data = MyCilmaTv.tvResult(val['title'])
                genres = tv_data['genres']
                language = tv_data['language']
                overview = tv_data['overview']

            match_result = {
                "title": val['title'],
                "original_release_year": val['original_release_year'],
                "poster_url": ''.join(poster_url),
                "hotstar_url": hotstar_url,
                "netflix_url": netflix_url,
                "prime_url": prime_url,
                "rt_rating": rt_rating,
                "imdb_rating": imdb_rating,
                "tmdb_rating": tmdb_rating,
                "overview": overview,
                "genres": genres,
                "language": language
            }
            break
        return match_result
