from rotten_tomatoes_client import RottenTomatoesClient


def getRottenRating(title_name):
    result = RottenTomatoesClient.search(term=title_name, limit=1)
    rating = "NA"
    for movies in result['movies']:
        rating = movies['meterScore']

    return str(rating)
