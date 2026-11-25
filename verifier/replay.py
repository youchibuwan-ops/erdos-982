"""Rebuild the archived DIMACS inputs and independently replay the RUP proofs."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
from dataclasses import dataclass
import gzip
from hashlib import sha256
from itertools import combinations_with_replacement, product
import json
import lzma
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from dense_lrat import renumber

@dataclass(frozen=True)
class Case:
    family: str
    label: str
    generator: Path
    arguments: tuple
    proof: Path
    hashes: dict
    core: Path | None = None


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return sha256(data).hexdigest()


def tsv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def labels(records, field, expected):
    actual = [record[field] for record in records]
    require(len(actual) == len(set(actual)) and set(actual) == set(expected),
            f"incomplete or duplicate branch list: {actual}")


def cases(root):
    main = root / "Erdos982_3_to_19"
    earlier = main / "earlier"
    old_labels = {
        "-".join(map(str, (a, b, n-a-b)))
        for n in range(6, 17, 2) for a in range(1, n // 2)
        for b in range(1, a + 1) if 1 <= n-a-b <= b
    }
    require({p.name.removesuffix(".rup.gz") for p in (earlier / "proofs").glob("*")}
            == old_labels, "early branch coverage")
    for tag in sorted(old_labels):
        yield Case("earlier", tag, earlier / "model.py", (), earlier / "proofs" /
                   f"{tag}.rup.gz", {})

    folder = main / "n18"
    records = tsv(folder / "manifest.tsv")
    labels(records, "gaps", ("882", "873", "864", "855", "774", "765"))
    for row in records:
        tag = row["gaps"]
        yield Case("n18", tag, folder / "generate.py", tuple(tag),
                   folder / f"{tag}.rup",
                   {"cnf_sha256": row["CNF_SHA256"], "rup_sha256": row["RUP_SHA256"],
                    "clauses": row["clauses"], "rup_steps": row["RUP_steps"]})

    folder = main / "n18-balanced"
    records = json.loads((folder / "manifest.json").read_text())["cases"]
    require(set(records) == {"EE", "ES", "SE", "SS"}, "balanced branch coverage")
    for tag, row in records.items():
        yield Case("n18-balanced", tag, folder / "generate18.py",
                   ("6", "6", "6", "{output}", tag.lower()), folder / f"{tag}.rup.xz", row)

    round3 = root / "round3"
    folder = round3 / "n20_992_983"
    records = tsv(folder / "manifest.tsv")
    labels(records, "case", ("992", "983"))
    for row in records:
        tag = row["case"]
        yield Case("n20_992_983", tag, folder / "generate.py", tuple(tag),
                   folder / f"{tag}.rup", row, folder / f"{tag}.core")

    nine = {"000", "100", "101", "110", "201", "210"}
    expected = {
        "n20_974": (nine - {"210"}) | {"210_6", "210_7"},
        "n20_965": {"000", "101", "110"} | {
            f"{order}_{rank}" for order, rank in product(("100", "201", "210"), (5, 6, 7))
            if (order, rank) != ("210", 6)
        } | {f"210_6{x}" for x in (5, 6, 7, 40, 41, 42, 43, 44, 45)},
        "n21_885_seven": {"000", "001", "100", "101", "102", "201", "210"},
        "n21_885_isosceles": {"7"} | {f"8{x}" for x in range(8)},
    }
    for family, tags in expected.items():
        folder = round3 / family
        records = tsv(folder / "manifest.tsv")
        key = next(iter(records[0]))
        labels(records, key, tags)
        for row in records:
            tag = row[key]
            order, _, branch = tag.partition("_")
            if family.endswith("isosceles"):
                args = (tag,)
            elif family.endswith("seven"):
                args = ("885", tag, "-", "disk")
            else:
                args = (family[-3:], order, branch or "-", "split")
            row["rup_sha256"] = row.get("rup_sha256") or row["proof_sha256"]
            row["rup_steps"] = row.get("rup_steps") or row.get("RUP_steps") or row["RUP_additions"]
            yield Case(family, tag, folder / "generate.py", args, folder / f"{tag}.rup",
                       row, folder / f"{tag}.core")

    weak_orders = {t for t in product((1, 2, 3), repeat=3)
                   if set(t) == set(range(1, max(t) + 1))}
    for family, tags in {
        "n21_876": {"".join(map(str, t)) for t in weak_orders},
        "n21_777": {"211", "221", "321"} | {
            "eq" + "".join(map(str, t))
            for t in combinations_with_replacement((6, 7, 8), 3)},
    }.items():
        folder = round3 / family
        require({p.name for p in folder.iterdir() if p.is_dir()} == tags,
                f"incomplete {family} branch list")
        for tag in sorted(tags):
            branch = folder / tag
            row = json.loads((branch / "manifest.json").read_text())
            require(row["case"] == tag, f"mislabeled {branch}")
            row["cnf_sha256"] = row["formula_sha256"]
            yield Case(family, tag, folder / "generate.py", (tag,), branch / "proof.rup.xz",
                       row, branch / "axioms.txt")

    folder = round3 / "n22_886"
    hashes = {name: checksum for checksum, name in
              map(str.split, (folder / "SHA256SUMS").read_text().splitlines())}
    yield Case("n22_886", "886", folder / "generate.py", (), folder / "886.rup", {
        "cnf_sha256": hashes["886.cnf"], "core_sha256": hashes["886.core"],
        "rup_sha256": hashes["886.rup"], "variables": 12936, "clauses": 506769,
        "core_axioms": 22307, "rup_steps": 32628}, folder / "886.core")

    folder = root / "n20_884_cert"
    require(folder.is_dir(), "missing n20_884_cert directory")
    expected_884 = {"000", "001", "100", "101", "102", "201", "110_7"}
    expected_884.update(f"210_{x}" for x in range(8))
    expected_884.update(f"110_8{x}" for x in range(5))
    expected_884.update(f"110_8{x}{y}" for x, y in combinations_with_replacement(range(5, 8), 2))
    rows = tsv(folder / "manifest.tsv")
    labels(rows, "tag", expected_884)
    for row in rows:
        tag = row["tag"]
        yield Case("n20_884", tag, folder / "generate.py",
                   ("884", row["subtype"], row["branch"], "disk"),
                   folder / f"{tag}.rup.xz", row)

    folder = root / "n20_initial"
    require(folder.is_dir(), "missing n20_initial directory")
    published = {
        "9-9-2": ("85679c3067f14e149d7584eb6f0278a7b9dce7c79cd8ef38ce0b0498c952448b",
                  "4869718cbdc3140739d4a354b13f70234482ec9d5c3194c605693a0cc1331387", 17561),
        "9-8-3": ("3ca5cc4a372ee185d3166043e3993e4e907f6ade1354334a3162184832ae8e21",
                  "f642c649b00edc60642e82fba0d057fb805559c3c2b839a4d82b7c6919829a65", 288997),
    }
    for tag, (formula, proof, steps) in published.items():
        yield Case("n20_initial", tag, folder / "generate.py", (tag,),
                   folder / f"{tag}.rup.xz",
                   {"cnf_sha256": formula, "rup_sha256": proof, "rup_steps": steps})


def compare(case, field, actual):
    value = case.hashes.get(field)
    require(value is None or str(actual) == str(value),
            f"{case.family}/{case.label}: {field} got {actual}, expected {value}")


def make_formula(case, output):
    if case.family == "earlier":
        code = ("import pathlib,sys; from model import make_model; "
                "from model16 import make_cnf; g=tuple(map(int,sys.argv[1].split('-'))); "
                "n=sum(g); s=make_cnf(g) if n==16 else make_model(g,global_order=n>10).dimacs(); "
                "pathlib.Path(sys.argv[2]).write_bytes(s.encode('ascii'))")
        command = ["-c", code, case.label, str(output)]
    else:
        args = [str(output) if arg == "{output}" else arg for arg in case.arguments]
        if "{output}" not in case.arguments:
            args.append(str(output))
        command = [str(case.generator), *args]
    subprocess.run([sys.executable, *command], cwd=case.generator.parent, check=True)
    data = output.read_bytes().replace(b"\r\n", b"\n")
    compare(case, "cnf_sha256", digest(data))
    header, *lines = data.splitlines()
    magic, kind, variables, total = header.split()
    require((magic, kind) == (b"p", b"cnf") and len(lines) == int(total), "invalid DIMACS header")
    compare(case, "variables", int(variables))
    compare(case, "clauses", int(total))
    if case.core is not None:
        core = case.core.read_bytes()
        compare(case, "core_sha256", digest(core))
        ids = list(map(int, core.split()))
        require(ids and len(ids) == len(set(ids)) and min(ids) >= 1 and max(ids) <= len(lines),
                "invalid or duplicated one-based core ID")
        compare(case, "core_axioms", len(ids))
        selected = [f"p cnf {int(variables)} {len(ids)}".encode()]
        selected.extend(lines[i - 1] for i in sorted(ids))
        output.write_bytes(b"\n".join(selected) + b"\n")
    else:
        output.write_bytes(data)
    return digest(data), digest(output.read_bytes())


def replay(case, checker, drat, lrat_check, lean_checker, log, keep):
    identifier = f"{case.family}/{case.label}"
    with tempfile.TemporaryDirectory() as name:
        work = Path(name)
        formula, trace, hints = (work / p for p in ("input.cnf", "proof.rup", "proof.lrat"))
        cnf_hash, core_hash = make_formula(case, formula)
        packed = case.proof.read_bytes()
        if case.proof.suffix == ".xz":
            compare(case, "xz_sha256", digest(packed))
            proof = lzma.decompress(packed)
        elif case.proof.suffix == ".gz":
            proof = gzip.decompress(packed)
        else:
            proof = packed
        proof_hash = digest(proof)
        compare(case, "rup_sha256", proof_hash)
        rows = proof.splitlines()
        require(rows and rows[-1].strip() == b"0", f"{identifier}: final empty clause missing")
        with formula.open("rb") as stream:
            nvars = int(stream.readline().split()[2])
        steps = 0
        for index, line in enumerate(rows, 1):
            if not line.strip() or line.startswith((b"c", b"i", b"d")):
                continue
            literals = [int(x) for x in line.split()]
            require(literals[-1] == 0 and all(0 < abs(x) <= nvars for x in literals[:-1])
                    and (len(literals) > 1 or index == len(rows)),
                    f"{identifier}: invalid proof syntax at line {index}")
            steps += 1
        compare(case, "rup_steps", steps)
        trace.write_bytes(proof)
        methods = []
        if checker is not None:
            result = subprocess.run([checker, formula, trace], capture_output=True, text=True, check=True)
            require(re.search(rf"UNSAT \({steps} (?:RUP )?steps\)", result.stdout),
                    f"{identifier}: unexpected checker output {result.stdout}")
            methods.append("forward-rup")
        if drat is not None:
            # DRAT-trim uses SAT-solver exit conventions and may exit zero on failure.
            result = subprocess.run([drat, formula, trace, "-U", "-L", hints],
                                    capture_output=True, text=True)
            require("s VERIFIED" in result.stdout and
                    re.search(r"\b0 RAT lemmas\b", result.stdout) and hints.is_file(),
                    f"{identifier}: DRAT-trim did not verify: {result.stdout[-2000:]}")
            result = subprocess.run([lrat_check, formula, hints], capture_output=True, text=True)
            require(result.returncode == 0 and re.search(r"(?m)^c VERIFIED\s*$", result.stdout),
                    f"{identifier}: lrat-check did not verify: {result.stdout[-2000:]}")
            methods.append("drat-trim-rup+lrat-check")
            if lean_checker is not None:
                dense = work / "dense.lrat"
                renumber(formula, hints, dense)
                result = subprocess.run([lean_checker, formula, dense], capture_output=True, text=True)
                require(result.returncode == 0 and result.stdout.startswith("VERIFIED "),
                        f"{identifier}: Lean exit {result.returncode}: "
                        f"{result.stdout[-2000:]} {result.stderr[-2000:]}")
                methods.append("lean-verified-checker")
            if keep is not None:
                folder = keep / case.family / case.label
                folder.mkdir(parents=True, exist_ok=True)
                (folder / "input.cnf").write_bytes(formula.read_bytes())
                shutil.move(hints, folder / "proof.lrat")
        record = {"family": case.family, "case": case.label, "cnf_sha256": cnf_hash,
                  "checked_cnf_sha256": core_hash, "rup_sha256": proof_hash,
                  "rup_steps": steps, "methods": methods}
        (log / f"{case.family}-{case.label}.json").write_text(json.dumps(record) + "\n")
        print(identifier, steps, ",".join(methods), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="directory of unpacked source packages")
    parser.add_argument("--checker", type=Path, help="compiled forward checker")
    parser.add_argument("--drat", type=Path)
    parser.add_argument("--lrat-check", type=Path)
    parser.add_argument("--lean-checker", type=Path)
    parser.add_argument("--keep-lrat", type=Path)
    parser.add_argument("--family", action="append")
    parser.add_argument("--case", action="append")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()
    if not args.checker and not (args.drat and args.lrat_check):
        parser.error("provide a forward checker or both independent LRAT tools")
    if bool(args.drat) != bool(args.lrat_check) or (args.lean_checker and not args.drat):
        parser.error("LRAT replay requires both DRAT-trim and lrat-check")
    paths = [path.resolve() if path else None for path in
             (args.checker, args.drat, args.lrat_check, args.lean_checker)]
    selected = [c for c in cases(args.root.resolve())
                if (not args.family or c.family in args.family)
                and (not args.case or c.label in args.case)]
    require(selected, "no matching case")
    args.log.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        pending = {pool.submit(replay, c, *paths, args.log, args.keep_lrat): c for c in selected}
        failed = 0
        for item in as_completed(pending):
            try:
                item.result()
            except Exception as error:
                case = pending[item]
                print(f"FAILED {case.family}/{case.label}: {error}", file=sys.stderr, flush=True)
                failed += 1
    if failed:
        sys.exit(f"{failed} of {len(selected)} cases failed")


if __name__ == "__main__":
    main()
