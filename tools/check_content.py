"""Validate publication boundaries, explicit TOC, MyST source links, and labels."""
from pathlib import Path
import re
import sys
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ("course", "hardware", "reference", "educators", "contributing")


def pages():
    config = yaml.safe_load((ROOT / "myst.yml").read_text(encoding="utf-8"))
    result = []

    def walk(entries):
        for entry in entries:
            if "file" in entry:
                result.append(ROOT / entry["file"])
            walk(entry.get("children", []))
    walk(config["project"]["toc"])
    return result


def source(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".ipynb":
        return "\n".join("".join(c["source"]) for c in json.loads(text)["cells"]
                         if c["cell_type"] == "markdown")
    return text


def main():
    errors, labels = [], {}
    listed = pages()
    expected = {ROOT / "index.md"} | {p for d in PUBLIC for p in (ROOT / d).rglob("*")
                                        if p.suffix in (".md", ".ipynb")}
    if len(listed) != len(set(listed)):
        errors.append("Duplicate TOC file")
    for path in set(listed) ^ expected:
        errors.append(f"TOC/publication mismatch: {path.relative_to(ROOT)}")
    for path in listed:
        if not path.exists():
            errors.append(f"Missing TOC target: {path}")
            continue
        body = source(path)
        for label in re.findall(r"^\(([^)]+)\)=$|^:label:\s*(\S+)", body, re.M):
            name = next(x for x in label if x)
            if name in labels:
                errors.append(f"Duplicate label {name}: {path} and {labels[name]}")
            labels[name] = path
        targets = re.findall(r"\]\(([^)\s]+)\)", body)
        targets += re.findall(r"\{(?:literalinclude|include|image|figure)\}\s+([^\s]+)", body)
        for target in targets:
            if target.startswith(("http:", "https:", "#", "mailto:", "<")):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"Missing/unsafe source target {target} in {path}")
        for match in re.finditer(r"\{literalinclude\}\s+([^\s]+)", body):
            included = (path.parent / match.group(1)).resolve()
            if included.exists() and included.suffix == ".py":
                try:
                    compile(included.read_text(encoding="utf-8"), str(included), "exec")
                except SyntaxError as exc:
                    errors.append(f"Invalid included Python: {exc}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(listed)} published pages and {len(labels)} explicit labels")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
