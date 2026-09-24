"""Check static HTML href/src assets and internal fragments under a selected base."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src", "poster"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if attrs.get("srcset"):
            self.links.extend(part.strip().split()[0] for part in attrs["srcset"].split(","))


def check(root, base):
    parsed, errors = {}, set()
    for path in root.rglob("*.html"):
        parser = Links()
        parser.feed(path.read_text(encoding="utf-8"))
        parsed[path.resolve()] = parser
    if not parsed:
        return ["No HTML files found"]
    for path, parser in parsed.items():
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            route = unquote(url.path)
            if route.startswith("/"):
                if base and route != base and not route.startswith(base + "/"):
                    errors.add(f"{path.name}: URL escapes base {base}: {link}")
                    continue
                target = root / route[len(base):].lstrip("/")
            else:
                target = path.parent / route if route else path
            if target.is_dir():
                target = target / "index.html"
            if not target.exists() and not target.suffix:
                target = target.with_suffix(".html")
            if not target.exists():
                errors.add(f"{path.relative_to(root)}: missing {link}")
                continue
            dest = parsed.get(target.resolve())
            if url.fragment and dest and unquote(url.fragment) not in dest.ids:
                errors.add(f"{path.relative_to(root)}: missing fragment {link}")
    # Publication must not expose source-only directories as navigable pages.
    for path in parsed:
        relative = path.relative_to(root).parts
        if relative[0] in ("research", "design", "student-work", "tools", "tests", "examples"):
            errors.add(f"Internal page published: {path.relative_to(root)}")
    print(f"Checked {len(parsed)} HTML pages with base {base or '/'}")
    return sorted(errors)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("_build/html"))
    parser.add_argument("--base", default="")
    args = parser.parse_args()
    failures = check(args.root.resolve(), args.base.rstrip("/"))
    if failures:
        raise SystemExit("\n".join(failures))
