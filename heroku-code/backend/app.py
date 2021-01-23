from backend.search import search
from backend.services import services
from flask import Flask, Response
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
APP = Flask(__name__)
CORS(APP)
API = Api(APP)

parser = reqparse.RequestParser()

class ResponseList(Resource):
  def get(self):
    parser.add_argument("q")
    args = parser.parse_args()
    try:
      out = str(json.dumps(
        search(args['q']),
        default=lambda o: o.__dict__,
        sort_keys=True
      ))
    except Exception as err:
      print(err)
      return 500
    return out, 200

class ServicesList(Resource):
  def get(self):
    try:
      out = str(json.dumps(
        list(services.keys()),
        sort_keys=True
      ))
    except Exception as err:
      print(err)
      return 500
    return out, 200

API.add_resource(ResponseList, '/search/')
API.add_resource(ServicesList, '/services/')

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)