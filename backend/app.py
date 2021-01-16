import flask
from flask import json, Response
from flask_cors import CORS
from flask_api import FlaskAPI
from search import Search
APP = FlaskAPI(__name__)
CORS(APP)



if __name__ == '__main__':
  APP.run(host='127.0.0.1', port=9000)
