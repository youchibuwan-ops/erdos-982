# Lean checks

This project uses Lean 4.33.1 and Std's LRAT implementation. Build from the repository root with the toolchain pinned here:

~~~sh
cd lean
lean Profiles.lean
lean -c CheckLrat.c CheckLrat.lean
leanc -O3 CheckLrat.c -o checklrat
~~~

Then add **--lean-checker lean/checklrat** to the replay command from the repository root. The executable verifies unsatisfiability of the parsed CNF against dense LRAT hints. DRAT-trim can skip IDs when emitting only proof steps used in the contradiction. Lean Std appends clauses by position. The driver renumbers included additions and rewrites all hints and deletions, then checks the rewritten trace with Lean.

All 126 archived refutations passed this path. The [per-branch results](../certificates/replay.json) include the canonical 124 traces and the two historical alternatives.

The axiom query for **support20**, **support21Short**, and **support22Short** reports no axioms. These theorems check finite lists of integer partitions. The query for **Std.Tactic.BVDecide.LRAT.check_sound** reports **propext**, **Classical.choice**, and **Quot.sound**. The CLI runs the checker compiled to native code. Its bridge from DIMACS bytes to the internal CNF, the compiler/runtime and the execution environment are part of the trusted base. This path yields executable certificate checks. It does not elaborate a separate theorem for each archived file.

An external end-to-end Lean project covers \(3\le n\le13\), with source statement checks against Google DeepMind Formal Conjectures and explicit native-computation axioms at refutation lemmas. This audit inspected the fixed source revision. The present geometry-to-CNF implication is a conventional proof, so imported CNF checks do not constitute end-to-end formalization of the original statements here. [Quantavane fixed revision](https://github.com/arhancanli/quantavane-lean/tree/76a54a6c728161e75e1b0275c0b32ffc311f1f6a/erdos982-le13)
