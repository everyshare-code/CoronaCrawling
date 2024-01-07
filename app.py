from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.corona_news import Corona
from api.index import Index
import os


TEMPLATE_FOLDER=os.path.join(os.getcwd(),'front-end')


app=Flask(__name__,template_folder=TEMPLATE_FOLDER,static_folder=TEMPLATE_FOLDER,static_url_path='')
CORS(app)

api=Api(app)

api.add_resource(Corona,'/corona')
api.add_resource(Index,'/')

if __name__=='__main__':
    app.run(debug=True)

