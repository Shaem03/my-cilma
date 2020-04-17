import urllib.request

from bs4 import BeautifulSoup
from flask import Flask
from imdb import IMDb

application = Flask(__name__)
rest_server_port = 5000


def getImdbRating(title_name):
    rating = "NA"
    try:
        ia = IMDb()
        movie = ia.search_movie(title_name)
        for result in movie:
            if str(result).lower() == title_name.lower():
                title = result.movieID
                with urllib.request.urlopen("https://www.imdb.com/title/tt%s" % title) as url:
                    movie_data = url.read()
                break

        if movie_data:
            try:
                soup = BeautifulSoup(movie_data, features="lxml")
                for span in soup.findAll('span'):
                    if span.has_attr('itemprop') and span['itemprop'] == 'ratingValue':
                        rating = span.contents[0] + '/10'
                        break
            except:
                pass
        return rating
    except:
        return rating
