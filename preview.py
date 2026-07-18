"""Preview the site the way GitHub Pages serves it: make preview"""
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        f = super().translate_path(path)
        if not os.path.exists(f) and os.path.exists(f + ".html"):
            return f + ".html"
        return f


HTTPServer(("", 8000), Handler).serve_forever()
