from flask import Flask, jsonify
from flask_restplus import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)


def init_db():
    pass


@api.route('/reporting/articles/summary')
class Article(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run(debug=True)

