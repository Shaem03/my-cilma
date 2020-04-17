from flask import Flask, request

from availability_check import movieResult
from getMovie import searchMovies

application = Flask(__name__)
rest_server_port = 5000


@application.route("/silma-rating", methods=['GET'])
def cilmaRating():
    search_input = "titanic"
    search_input = request.args.get('name', default="", type=str)
    # tmdb_response = searchMovies(search_input)
    # imdb = getImdbRating(tmdb_response['title'])
    # rotten = getRottenRating(tmdb_response['title'])
    # rating_response = {
    #     'imdb_rating': imdb,
    #     'rotten_tomatoes': rotten
    # }
    # tmdb_response.update(rating_response)
    try:
        response_detail = movieResult(search_input)
        tmdb_response = searchMovies(response_detail['title'])
        response_detail.update(tmdb_response)

        return response_detail, 200, {
            'Content-Type': 'application/json'}
    except Exception as e:
        return e.__doc__, 500, {
            'Content-Type': 'application/json'}


if __name__ == '__main__':
    application.run(debug=False, port=rest_server_port)
