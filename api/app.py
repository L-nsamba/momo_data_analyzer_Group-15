from http.server import BaseHTTPRequestHandler, HTTPServer
from POST import handle_post

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/transactions':
            handle_post(self)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

def run_server(port=5000):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Server running on http://127.0.0.1:{port}')
    print('Press Ctrl+C to stop')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()