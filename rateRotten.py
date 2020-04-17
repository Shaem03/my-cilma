from rotten_tomatoes_client import RottenTomatoesClient


def getRottenRating(title_name):
    rating = "NA"
    try:
        result = RottenTomatoesClient.search(term=title_name, limit=1)
        for movies in result['movies']:
            rating = str(movies['meterScore']) + "%"
        return rating
    except:
        return rating
