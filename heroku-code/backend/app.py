from backend.search import search
from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
APP = Flask(__name__)
API = Api(APP)

parser = reqparse.RequestParser()

class ResponseList(Resource):
  def get(self):
    parser.add_argument("q")
    args = parser.parse_args()
    try:
      out = json.dumps(
        search(args['q']),
        default=lambda o: o.__dict__,
        sort_keys=True
      )
    except Exception as err:
      print(err)
      return '', 500
    return out, 200

API.add_resource(ResponseList, '/search/')

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)