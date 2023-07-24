from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Pong!</h1>')

        elif self.path == '/password':
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Sample password for now</h1>')
        else:
            self.send_response(404)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')
