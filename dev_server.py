"""Purpose: local no-cache dev server for Tailor Maciel website previews.
Date: 2026-05-07
Author: Codex for Tailor Maciel
Domain: Branding
"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.headers.replace_header("If-Modified-Since", "") if "If-Modified-Since" in self.headers else None
        self.headers.replace_header("If-None-Match", "") if "If-None-Match" in self.headers else None
        super().do_GET()

    def do_HEAD(self):
        self.headers.replace_header("If-Modified-Since", "") if "If-Modified-Since" in self.headers else None
        self.headers.replace_header("If-None-Match", "") if "If-None-Match" in self.headers else None
        super().do_HEAD()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8002), NoCacheHandler)
    print("Serving Tailor Maciel site at http://127.0.0.1:8002/ with no-cache headers")
    server.serve_forever()
