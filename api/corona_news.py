from flask_restful import Resource,reqparse
from flask import make_response
from model.corona_news_crawl import crawling
import json


class Corona(Resource):

    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('category',required=False,location='args')

        # parser.add_argument('page')
        args=parser.parse_args()
        print(args)
        contents=crawling(args)

        return make_response(json.dumps(contents,ensure_ascii=False))