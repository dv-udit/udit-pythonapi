from http.server import HTTPServer
from server.endpoints import Handler

def run():
    host = 'localhost'
    port = 8080

    server = HTTPServer((host,port),Handler)

    print(f"Server is running on http://{host}:{port}")


    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server is shutting down")
        
        server.server_close()


if __name__ == '__main__':
    run()