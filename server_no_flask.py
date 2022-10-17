import http.server
import socketserver
import json
from http import HTTPStatus

json_data = open('complex_response.json')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def do_GET(self):
        if self.path == '/simple/':
            data = bytes('hello world'.encode())
        else:
            data = json.dumps(json_data)
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(data)

if __name__ == "__main__":
    PORT = 8001
    server = socketserver.TCPServer(("localhost", PORT), Handler)
    print(f"server started at {PORT}")
    server.serve_forever()
