import sys
from pathlib import Path
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "verifier"))
from dense_lrat import renumber
from replay import labels


class CertificateControls(unittest.TestCase):
    def test_rejects_empty_and_duplicate_manifests(self):
        for rows in ([], [{"branch": "a"}, {"branch": "a"}]):
            with self.assertRaisesRegex(ValueError, "duplicate branch list"):
                labels(rows, "branch", {"a", "b"})
        labels([{"branch": "b"}, {"branch": "a"}], "branch", {"a", "b"})

    def test_sparse_ids_and_deletions(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            cnf, lrat, dense = [root / f for f in ("a.cnf", "a.lrat", "dense.lrat")]
            cnf.write_bytes(b"p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n")
            lrat.write_bytes(b"8 1 0 1 2 0\n8 d 1 2 0\n13 0 8 3 4 0\n")
            renumber(cnf, lrat, dense)
            self.assertEqual(dense.read_bytes(), b"5 1 0 1 2 0\n5 d 1 2 0\n6 0 5 3 4 0\n")
            lrat.write_bytes(b"8 0 13 0\n")
            with self.assertRaises(KeyError):
                renumber(cnf, lrat, root / "invalid.lrat")


if __name__ == "__main__":
    unittest.main()
