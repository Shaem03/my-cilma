from justwatch import JustWatch


def movieResult(input_string):
    just_watch = JustWatch(country='IN')
    # input_string = "hachiko"

    results = just_watch.search_for_item(query=input_string)
    for val in results['items']:
        hotstar_url = "NA"
        netflix_url = "NA"
        prime_url = "NA"
        rt_rating = "NA"
        imdb_rating = "NA"
        tmdb_rating = "NA"
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

            if ratings['provider_type'] == "tomato:meter":
                rt_rating = ratings['value']
            elif ratings['provider_type'] == "imdb:score":
                imdb_rating = ratings['value']
            elif ratings['provider_type'] == "tmdb:score":
                tmdb_rating = ratings['value']

        poster_url = "https://images.justwatch.com%ss592" % val['poster'][:-9],

        match_result = {
            "title": val['title'],
            "original_release_year": val['original_release_year'],
            "poster_url": ''.join(poster_url),
            "hotstar_url": hotstar_url,
            "netflix_url": netflix_url,
            "prime_url":prime_url,
            "rt_rating": rt_rating,
            "imdb_rating": imdb_rating,
            "tmdb_rating": tmdb_rating
        }
        break
    return match_result


# movieResult()
