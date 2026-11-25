"""Stage the audited source packages after checking every source byte."""

import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import zipfile


MANIFEST = Path(__file__).resolve().parents[1] / "research_logs" / "sources.json"


def check(data, item):
    if len(data) != item["bytes"] or sha256(data).hexdigest() != item["sha256"]:
        raise ValueError(f"source mismatch: {item['source']}/{item['path']}")


def write(destination, data):
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as stream:
        stream.write(data)


def safe_name(name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name or ":" in name:
        raise ValueError(f"invalid archive member: {name}")
    return path


def unpack(data, inventory, archive, destination, nested=None):
    paths = set()
    with zipfile.ZipFile(BytesIO(data)) as bundle:
        for info in bundle.infolist():
            path = safe_name(info.filename)
            if info.is_dir():
                continue
            if info.external_attr >> 16 & 0o170000 == 0o120000 or path in paths:
                raise ValueError(f"invalid archive entry {path}")
            paths.add(path)
            entry = f"{archive}!/{path}"
            content = bundle.read(info)
            check(content, inventory[("proof-packs", entry)])
            write(destination.joinpath(*path.parts), content)
            if nested is not None and path.suffix == ".zip":
                unpack(content, inventory, entry, nested / path.stem)
    expected = {name.split("!/", archive.count("!/") + 1)[-1] for source, name in inventory
                if source == "proof-packs" and name.startswith(archive + "!/")
                and name.count("!/") == archive.count("!/") + 1}
    if {str(path) for path in paths} != expected:
        raise ValueError(f"archive inventory mismatch: {archive}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--proof-packs", type=Path, required=True)
    parser.add_argument("--n20-884", type=Path, required=True)
    parser.add_argument("--n20-initial", type=Path, required=True)
    args = parser.parse_args()
    records = json.loads(MANIFEST.read_text(encoding="utf-8"))
    inventory = {(item["source"], item["path"]): item for item in records}
    args.destination.mkdir(parents=True)
    for name in ("Erdos982_3_to_19.zip", "Erdos982_round3.zip"):
        data = (args.proof_packs / name).read_bytes()
        check(data, inventory[("proof-packs", name)])
        unpack(data, inventory, name, args.destination / Path(name).stem,
               args.destination / "round3" if "round3" in name else None)
    for source, prefix, directory, family in (
        ("gemini", "n20_884_cert", args.n20_884, "n20_884_cert"),
        ("workspace", "erdos-982-n20", args.n20_initial, "n20_initial"),
    ):
        for (group, name), item in inventory.items():
            if group != source or not name.startswith(prefix + "/"):
                continue
            relative = safe_name(name.removeprefix(prefix + "/"))
            data = directory.joinpath(*relative.parts).read_bytes()
            check(data, item)
            write(args.destination.joinpath(family, *relative.parts), data)


if __name__ == "__main__":
    main()
