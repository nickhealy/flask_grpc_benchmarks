import json
from wsgiref.simple_server import make_server

complex_res = open('complex_response.json', 'r')
complex_json = json.load(complex_res)
complex_bytes = bytes(json.dumps(complex_json), 'utf-8')
complex_headers = [('Content-Type', 'application/json'), ('Content-Length', str(len(complex_bytes)))]

def application(environ, start_response):

    status = '200 OK'
    headers = []
    path = environ['PATH_INFO']
    data = b'empty_response'
    if path == '/simple/':
        data =  b"Hello, World"
    elif path == '/complex/':
        data = complex_bytes 
        headers = complex_headers
    start_response(status, headers)
    return [data]

