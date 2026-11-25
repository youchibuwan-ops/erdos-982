"""Render or check the human-readable register from its JSON source."""

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"LITERATURE", "REPROVED", "REVIEWED", "COMPUTER_ASSISTED", "REPRODUCED",
            "DRAFT", "SUPERSEDED", "REFUTED", "OPEN", "PARTIAL", "MISSING_SOURCE"}


def render(records):
    identifiers = [item["id"] for item in records]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("duplicate result ID")
    sections = [
        "# Results register\n",
        "The [JSON register](results.json) is the source of record. "
        "Geometry, numerical replay, Lean checks and priority are tracked per entry. "
        "A reviewed result has an independently checked mathematical argument in this repository. "
        "Draft status includes claims with substantial earlier review where first-pass adjudication is incomplete.\n",
        r"Here \(d_P(p)\) counts positive distances from pin \(p\), \(D(P)\) is the largest pin "
        r"count, and \(f(n)\) minimizes that maximum over strictly convex Euclidean \(n\)-point sets." + "\n",
    ]
    for row in records:
        code = row["id"]
        status = row["math_status"]
        if not re.fullmatch(r"982-[A-Z][0-9]{2}", code) or status not in STATUSES:
            raise ValueError((code, status))
        source = " · ".join(row["sources"])
        lines = [f"## {code} — {row['title']}\n", row["statement"] + "\n",
                 f"**{status}** · {row['computation']} · {row['lean']}\n",
                 f"Priority assessment — {row['originality']}.\n",
                 f"Source record — {source}\n",
                 f"Attribution — {row['contribution']}.\n"]
        if row["proof"]:
            if not (ROOT / row["proof"]).is_file():
                raise ValueError(f"missing proof path for {code}: {row['proof']}")
            lines.append(f"[Proof or audit]({row['proof']})\n")
        if row["dependencies"]:
            lines.append("Dependencies — " + " · ".join(row["dependencies"]) + "\n")
        if row["restrictions"]:
            lines.append(row["restrictions"] + "\n")
        sections.append("\n".join(lines))
    return "\n".join(sections)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    results = json.loads((ROOT / "results.json").read_text(encoding="utf-8"))
    target = ROOT / "RESULTS.md"
    document = render(results)
    if args.check:
        if document != target.read_text(encoding="utf-8"):
            raise SystemExit("RESULTS.md differs from results.json")
        print(f"{len(results)} unique registered results")
    else:
        target.write_text(document, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
