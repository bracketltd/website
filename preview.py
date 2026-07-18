"""Preview the site the way GitHub Pages serves it: make preview"""
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        f = super().translate_path(path)
        if not os.path.exists(f) and os.path.exists(f + ".html"):
            return f + ".html"
        return f

    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.exists("404.html"):
            self.error_message_format = open("404.html").read()
        super().send_error(code, message, explain)


HTTPServer(("", 8000), Handler).serve_forever()
