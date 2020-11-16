# Just Offer read/edit Kormoon ovEr Rest api
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import json


# Sample blog post data similar to
# https://ordina-jworks.github.io/frontend/2019/03/04/vue-with-typescript.html#4-how-to-write-your-first-component
PORT = 8000
get_data = {
    "location": "Building 3",
    "description": "Reuse from pop bus project",
    "counter": 0
}

poll_data = {

}


class _RequestHandler(BaseHTTPRequestHandler):
    # Borrowing from https://gist.github.com/nitaku/10d0662536f37a087e1b
    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path.strip() == "/poll":
            self.wfile.write(json.dumps(poll_data).encode('utf-8'))
        elif self.path.strip() == "/get":
            self.wfile.write(json.dumps(get_data).encode('utf-8'))

    def do_POST(self):
        global get_data, poll_data
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        if self.path.strip() == "/setpolldata":
            poll_data = message
        elif self.path.strip() == "/setmetadata":
            get_data = message
            # self._set_headers()
            # self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, _RequestHandler)
    print('Start J.O.K.E.R - INFORMATION SERVER at {}:{}'.format(
        server_address[0], server_address[1]))
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
