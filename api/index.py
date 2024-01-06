from flask_restful import Resource
from flask import make_response,render_template


class Index(Resource):
    def get(self):
        return make_response(render_template('index.html'),200)