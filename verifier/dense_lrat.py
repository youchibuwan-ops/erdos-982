"""Renumber the retained additions of a text RUP-only LRAT proof for Lean Std."""

from pathlib import Path


def renumber(formula: Path, source: Path, destination: Path) -> None:
    with formula.open("rb") as cnf:
        originals = int(cnf.readline().split()[3])
    new_ids = {}
    next_id = originals + 1

    def lookup(clause):
        if 0 < clause <= originals:
            return clause
        return new_ids[clause]

    with source.open("rb") as trace, destination.open("wb") as output:
        for line in trace:
            fields = line.split()
            if not fields or fields[0] == b"c":
                continue
            old_id, *terms = fields
            if terms[0] == b"d":
                mapped = [lookup(int(word)) for word in terms[1:-1]]
                if terms[-1] != b"0":
                    raise ValueError("unterminated LRAT deletion")
                row = [next_id - 1, "d", *mapped, 0]
            else:
                end = terms.index(b"0")
                if terms[-1] != b"0":
                    raise ValueError("unterminated LRAT hints")
                hints = [lookup(int(word)) for word in terms[end+1:-1]]
                number = int(old_id)
                if number <= originals or number in new_ids:
                    raise ValueError("reused LRAT addition ID")
                new_ids[number] = next_id
                row = [next_id, *map(int, terms[:end]), 0, *hints, 0]
                next_id += 1
            output.write((" ".join(map(str, row)) + "\n").encode("ascii"))
