from flask import Flask
from rateImdb import getImdbRating
from rateRotten import getRottenRating
import json

application = Flask(__name__)
rest_server_port = 5000


@application.route("/silma-rating", methods=['GET'])
def health():
    imdb = getImdbRating("the dark knight rises")
    rotten = getRottenRating("the dark knight rises")
    return json.dumps({'Movie': 'The Dark Knight Rises', 'imdb': imdb, 'rotten': rotten}), 200, {
        'Content-Type': 'application/json'}


if __name__ == '__main__':
    application.run(debug=False, port=rest_server_port)
