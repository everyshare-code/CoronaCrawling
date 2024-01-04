from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.corona_news import Corona

app=Flask(__name__)

CORS(app)

api=Api(app)

api.add_resource(Corona,'/corona')

if __name__=='__main__':
    app.run(debug=True)

