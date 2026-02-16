#!/usr/bin/python3
"""Task 02 - RESTful API - Python Requests"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

serv_adress = ("", PORT)
httpd = HTTPServer(serv_adress, SimpleHTTPRequestHandler)
httpd.serve_forever()
