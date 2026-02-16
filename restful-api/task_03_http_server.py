#!/usr/bin/python3
"""Task 02 - RESTful API - Python Requests"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            data1 = {"name": "John", "age": 30, "city": "New York"}
            data2 = {"version": "1.0", "description": "A simple API built with http.server"}
            if self.path == "/status":
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"OK")
            elif self.path == "/info":
                datas2 = json.dumps(data2)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(datas2.encode())
            elif self.path == "/data":
                datas1 = json.dumps(data1)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(datas1.encode())
            else:
                if self.path == "/":
                    self.send_response(200)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"Hello, this is a simple API!")
                else:
                    self.send_response(404)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"Endpoint not found")

serv_adress = ("", PORT)
httpd = HTTPServer(serv_adress, SimpleHTTPRequestHandler)
httpd.serve_forever()
