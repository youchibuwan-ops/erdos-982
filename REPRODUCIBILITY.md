# Reproducibility

The reference run used Windows Python 3.13.14 for source intake and exact examples, WSL Ubuntu Python 3.12 and GCC for the independent LRAT path, MinGW C++17 for the forward RUP path, and Lean 4.33.1 for the second LRAT checker. The arithmetic verifier depends on SymPy 1.14.0. The source archive hashes are part of the [inventory](research_logs/sources.json). Inputs remain outside release tarballs until rights and private links in the raw material have been checked.

## Exact checks and manuscript

From the repository root:

~~~sh
python -m pip install sympy==1.14.0
python -m unittest discover -s tests
python verifier/render_results.py --check
python verifier/bound_parameters.py
python examples/diameter_octagon.py
python examples/contact_octagon.py
tectonic manuscript.tex
~~~

The parameter checker evaluates the quadratics, two Sturm root counts and covering rational rectangles, whose square-root bounds are checked by integer squaring. The paper supplies the mathematical implication of those inequalities.

## Prepare the finite inputs

Pass the directory containing the original 3-to-19 and Round 3 ZIP files and the two supplemental 20-point directories. The destination must be fresh.

~~~sh
python verifier/prepare.py work/inputs \
  --proof-packs /path/to/proof-packs \
  --n20-884 /path/to/n20_884_cert \
  --n20-initial /path/to/erdos-982-n20
~~~

Preparation compares the supplied bytes to the inventory. It does not use the SAT search that found the proofs. Text DIMACS output is normalized to LF for manifest comparison, which fixes the Windows CRLF issue in the balanced 18-point cases. The supplied proof bytes and compressed copies retain their original identities.

## Independent replay

Use the pinned DRAT-trim revision and compile both tools from source. Then run the local driver.

~~~sh
git clone https://github.com/marijnheule/drat-trim.git work/drat-trim
git -C work/drat-trim checkout 2e3b2dc0ecf938addbd779d42877b6ed69d9a985
cc -O3 work/drat-trim/drat-trim.c -o work/drat-trim/drat-trim
cc -O3 work/drat-trim/lrat-check.c -o work/drat-trim/lrat-check
python verifier/replay.py work/inputs --jobs 6 \
  --drat work/drat-trim/drat-trim --lrat-check work/drat-trim/lrat-check \
  --log work/results
~~~

Use filters such as **--family earlier --case 4-3-3** for a small, nontrivial trace. A full run can take many minutes. The optional **--checker** flag runs a compiled forward checker on every addition. The project audit compiled and ran Gemini's independent implementation from source. The driver requires DRAT-trim's RUP-only verified verdict with zero RAT lemmas, a generated LRAT proof, and a separate lrat-check verdict. To retain exported hints for review use **--keep-lrat work/hints**.

The mathematical implication of the formulas is reviewed in [finite encoding](proofs/finite-encoding.md). See [Lean build and trust notes](lean/README.md) for Lean. GitHub Actions runs public-source exact and Lean controls plus the registry consistency check. Full certificate replay uses the separately staged original bundles.
