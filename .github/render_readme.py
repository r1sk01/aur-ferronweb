#!/usr/bin/env python3
"""Render README.md from .github/readme.tmpl.md and the current PKGBUILDs."""

import datetime
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
TMPL = ROOT / ".github" / "readme.tmpl.md"

ROWS = [
    ("ferron", "source", "latest stable"),
    ("ferron-bin", "prebuilt", "latest stable"),
    ("ferron-rc", "source", "release candidates"),
    ("ferron-git", "source", "`develop-3.x`"),
    ("ferronweb", "shim", "N/A"),
]


def field(pkg: str, key: str) -> str:
    text = (ROOT / "packages" / pkg / "PKGBUILD").read_text()
    match = re.search(rf"^{key}=(.*)$", text, re.M)
    if not match:
        raise SystemExit(f"{pkg}: no {key}=")
    return match.group(1).strip().strip("'\"")


def main() -> None:
    rows = []
    for pkg, build, follows in ROWS:
        version = f"{field(pkg, 'pkgver')}-{field(pkg, 'pkgrel')}"
        desc = field(pkg, "pkgdesc")
        rows.append(f"| [`{pkg}`](/packages/{pkg}) | {version} | {build} | {follows} | {desc} |")

    log = subprocess.run(
        ["git", "log", "-1", "--format=- %s"], cwd=ROOT,
        capture_output=True, text=True, check=False,
    )
    latest = log.stdout.strip() or "No changes."
    checked = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC")

    out = (
        TMPL.read_text()
        .replace("@ROWS@", "\n".join(rows))
        .replace("@CHECKED@", checked)
        .replace("@LATEST@", latest)
    )
    (ROOT / "README.md").write_text(out)
    print(out)


if __name__ == "__main__":
    main()
