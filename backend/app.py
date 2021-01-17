import flask
from flask import json, Response
from flask_cors import CORS
from flask_api import FlaskAPI
from search import Search
APP = FlaskAPI(__name__)
CORS(APP)

def get_json_response(filename):
    labels_dict = {}
    response_dict = {}
    try:
        with open(filename, 'r') as labels:
            labels_dict = json.load(labels)
        response_dict[STATUS] = "true"
        response_dict["labels_mapping"] = labels_dict
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump,status=200,
                        mimetype='application/json')
    except FileNotFoundError as err:
        response_dict = {'error': 'file not found in server'}
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump,status=500,
                        mimetype='application/json')
    except RuntimeError as err:
        response_dict = {'error': 'error occured on server side. Please try again'}
        js_dump = json.dumps(response_dict)
        resp = Response(js_dump, status=500,
                        mimetype='application/json')
    return resp

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000)
