from http.server import BaseHTTPRequestHandler, HTTPServer
from pkgUdit import generate_pass

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Pong!</h1>')

        elif self.path == '/password':
            password = generate_pass()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<h1>Password: {password}</h1>'.encode())

        else:
            self.send_response(404)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')

