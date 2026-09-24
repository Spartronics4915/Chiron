"""Scheduled, non-blocking-for-PR reference audit; write actionable failure URLs."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
from urllib.request import Request, urlopen
from check_content import pages, source

urls = sorted({u.rstrip(".,") for page in pages()
               for u in re.findall(r"https://[^\s<>\)\]\"`]+", source(page))})


def check(url):
    try:
        request = Request(url, headers={"User-Agent": "Chiron-course-reference-check/0.1"})
        with urlopen(request, timeout=25) as response:
            if response.status >= 400:
                return f"{response.status}: {url}"
    except Exception as exc:
        return f"{url}: {exc} (review manually; may be temporary or bot protection)"
    return None


with ThreadPoolExecutor(max_workers=4) as pool:
    failures = [result for result in pool.map(check, urls) if result]
report = Path("_build/reports/external-links.txt")
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text("\n".join(failures) or "All checked references responded successfully.\n",
                  encoding="utf-8")
print(f"Checked {len(urls)} URLs; {len(failures)} need review. See {report}.")
raise SystemExit(bool(failures))
