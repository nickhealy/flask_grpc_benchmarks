import json, orjson
from flask import Flask

app = Flask(__name__)

json_file = open('complex_response.json')
complex_res = json.load(json_file)

class ORJSONDecoder:

    def __init__(self, **kwargs):
        # eventually take into consideration when deserializing
        self.options = kwargs

    def decode(self, obj):
        return orjson.loads(obj)


class ORJSONEncoder:
    def __init__(self, **kwargs):
        self.options = kwargs

    def encode(self, obj):
        return orjson.dumps(obj)


@app.route('/simple/')
def simple():
    return 'hello world\n'

@app.route('/complex/')
def complex():
    return complex_res 

def create_app(use_orjson = False):
    if use_orjson:
        app.json_encoder = ORJSONEncoder
        app.json_decoder = ORJSONDecoder
    return app
