#!/usr/bin/env python3
"""Simple API server using http.server.

Endpoints:
 - /           : Plain text greeting
 - /data       : JSON payload with sample data
 - /status     : Plain text OK
 - /info       : JSON with basic meta info
 Any other path returns 404 with an error message.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status=200, body=b"", content_type="text/plain; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/" or path == "":
            msg = "Hello, this is a simple API!"
            self._send_response(200, msg.encode("utf-8"), "text/plain; charset=utf-8")
            return

        if path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(payload).encode("utf-8")
            self._send_response(200, body, "application/json; charset=utf-8")
            return

        if path == "/status":
            body = b"OK"
            self._send_response(200, body, "text/plain; charset=utf-8")
            return

        if path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            body = json.dumps(payload).encode("utf-8")
            self._send_response(200, body, "application/json; charset=utf-8")
            return

        # Unknown endpoint
        msg = "Endpoint not found"
        self._send_response(404, msg.encode("utf-8"), "text/plain; charset=utf-8")

    # Suppress default logging to keep output clean; override if needed
    def log_message(self, format, *args):
        return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == "__main__":
    run()
