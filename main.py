from flask import Flask, request
from rateImdb import getImdbRating
from rateRotten import getRottenRating
from getMovie import searchMovies

application = Flask(__name__)
rest_server_port = 5000


@application.route("/silma-rating", methods=['GET'])
def cilmaRating():
    search_input = "titanic"
    search_input = request.args.get('name', default="", type=str)
    tmdb_response = searchMovies(search_input)
    imdb = getImdbRating(tmdb_response['title'])
    rotten = getRottenRating(tmdb_response['title'])
    rating_response = {
        'imdb_rating': imdb,
        'rotten_tomatoes': rotten
    }
    tmdb_response.update(rating_response)
    print(tmdb_response)
    return tmdb_response, 200, {
        'Content-Type': 'application/json'}


if __name__ == '__main__':
    application.run(debug=False, port=rest_server_port)
