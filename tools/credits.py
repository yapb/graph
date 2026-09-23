#!/usr/bin/env python3
"""Generate CREDITS.md for the YaPB graph database.

The graph format does not need to be decompressed: the author nickname lives in
the trailing ExtenHeader, which can be located from the file header alone.

Binary layout of a .graph file:
    StorageHeader (24 bytes)   magic, version, options, length, compressed, uncompressed
    ULZ payload  (header.compressed bytes)
    ExtenHeader  (68 bytes, only when header.options & kStorageCreator is set)
        author[32], mapSize(int32), modified[32]

Used from the repository root::

    python tools/credits.py graph
"""

import argparse
import struct
import sys
from pathlib import Path

MAGIC = 0x59415042          # "BPAY"
MAGIC_UB = 0x544F4255       # "UBOT"
STORAGE_CREATOR = 0x40      # header.options bit pointing at the ExtenHeader

HEADER_SIZE = 24
AUTHOR_SIZE = 32
EXTEN_SIZE = 68

# original name -> displayed name
ALIASES = {
    "Владислав": "$_Vladislav",
    "Overitab": "Drevny13",
}
KEY_AUTHORS = {"$_Vladislav", "Drevny13", "[PRince4]", "DarkFlame"}


def read_author(path: Path):
    """Return the author stored in a .graph file, or None if it cannot be read."""
    try:
        with path.open("rb") as fp:
            blob = fp.read(HEADER_SIZE)
            if len(blob) < HEADER_SIZE:
                return None

            magic, _version, options, _length, compressed, _uncompressed = struct.unpack(
                "<6i", blob
            )

            if magic not in (MAGIC, MAGIC_UB):
                return None
            if not options & STORAGE_CREATOR:
                return None

            fp.seek(HEADER_SIZE + compressed)
            raw = fp.read(AUTHOR_SIZE)
    except OSError:
        return None

    return raw.split(b"\x00", 1)[0].decode("utf-8", "replace").strip()


def collect(folder: Path):
    key_credits = {}
    credits = {}

    for path in sorted(folder.rglob("*")):
        if not path.is_file() or "graph" not in path.name:
            continue

        author = read_author(path)
        if author is None:
            print(f"ERROR {path}", file=sys.stderr)
            continue

        # plain map name: the file name without the ".graph" suffix
        name = path.name
        if name.endswith(".graph"):
            name = name[:-6]

        author = ALIASES.get(author, author)
        bucket = key_credits if author in KEY_AUTHORS else credits
        bucket.setdefault(author, []).append(name)

    return key_credits, credits


def sort_credits(source):
    # by contributed count (desc), then by nickname
    return sorted(source.items(), key=lambda item: (-len(item[1]), item[0]))


def render(key_credits, credits) -> str:
    lines = ["# Credits for the waypoints"]

    for author, maps in sort_credits(key_credits) + sort_credits(credits):
        display = author or "Unknown"
        lines.append(f"## {display} (contributed {len(maps)})")
        lines.append(", ".join(maps))

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate CREDITS.md for the YaPB graph database."
    )
    parser.add_argument(
        "folder", nargs="?", default="graph", help="directory with .graph files"
    )
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"error: '{folder}' is not a directory", file=sys.stderr)
        return 1

    key_credits, credits = collect(folder)
    (Path.cwd() / "CREDITS.md").write_text(render(key_credits, credits), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
