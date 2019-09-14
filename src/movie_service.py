# Web-server
from flask import Flask
from flask_restplus import Api, Resource
from http import HTTPStatus
# Database
from pymongo import MongoClient
# Models
from src.models.movie import MOVIE

MONGO = MongoClient()

# Initialization Params
app = Flask(__name__)
api = Api(app)

# Registers models
MOVIE = api.model("Movie", MOVIE)


@api.route("/movies")
class AllMovies(Resource):
    records = MONGO.movies.records

    @api.marshal_with(MOVIE)
    def get(self):
        return list(movie for movie in self.records.find())


@api.route("/movies/<int:year>")
class MoviesByYear(Resource):
    records = MONGO.movies.records

    @api.marshal_with(MOVIE)
    def get(self, year: int):
        return list(movie for movie in self.records.find({"year": {"$eq": year}}))


if __name__ == "__main__":
    app.run(
        debug=True
    )
