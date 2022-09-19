import http.server
import socketserver

PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("ec2-54-190-2-135.us-west-2.compute.amazonaws.com", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
