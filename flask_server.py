import json
from flask import Flask

app = Flask(__name__)

json_file = open('complex_response.json')
complex_res = json.load(json_file)

@app.route('/simple/')
def simple():
    return 'hello world\n'

@app.route('/complex/')
def complex():
    return complex_res 

def create_app():
    return app
