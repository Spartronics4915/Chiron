"""Preview a static build at its actual hosting base, including directory URLs."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--base", default="")
parser.add_argument("--port", type=int, default=8000)
args = parser.parse_args()
base = args.base.rstrip("/")


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if base:
            if self.path != base and not self.path.startswith(base + "/"):
                self.send_error(404)
                return
            self.path = self.path[len(base):] or "/"
        super().do_GET()


print(f"Preview: http://localhost:{args.port}{base}/", flush=True)
ThreadingHTTPServer(("127.0.0.1", args.port), partial(
    Handler, directory=str(Path("_build/html").resolve()))).serve_forever()
