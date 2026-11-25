# Independent audit

## Scope and decision

The cumulative report is the intake index. The [source inventory](research_logs/sources.json) covers 83 original files and 369 archive entries, including nested proof ZIP members, with 404 distinct SHA-256 digests across 452 entries. The originals were left in place. Claims are in the [results register](RESULTS.md). Candidate originality is bounded by the [reference search](REFERENCES.md).

The first reviewed release set consists of the revised unrestricted bound, coordinate-field results, finite reductions with reproducible certificates, and the analytic arguments in the manuscript. The finite corpus remains split at 20. The original progress reports and earlier versions remain identifiable by hash.

## Corrections and negative controls

| Claim or component | Audit finding and current evidence |
| --- | --- |
| 982-G05, 982-G07 | The positive part of \((r-s)(r-9s)/8\) gives a spurious positive value at \(r=0\) when \(s>0\). The current proof sets the function to zero throughout \(r\le9s\). It bounds earlier intruders using the **current** cutoff and monotonicity in time. It accounts separately for surviving endpoints lost to deleted witnesses and the overlap cost. The original program has a fixed \(1/1674\) print at the end. The independent verifier confirms \(d=353/40000,\eta=3/1667\), 51,599 relevant rational rectangles, and minimum box margin \(48443/96000000\). |
| 982-F03 | The 21-point reduction only uses the four nine-leading 20-point profiles and three separately checked short-chain profiles. This leaves the 20-point gap. |
| 982-F04 | The 22-point bundle includes a separate certificate for ten distances on \((8,8,6)\). That threshold also follows by monotonicity from \(f(21)=10\). |
| 982-N05 | The November 25 audit documented that the original manifest-driven runner accepts an empty table as an empty successful run. The current driver compares the branch labels with the derived 26 labels and checks the actual proof counts. |
| 982-N06, 982-N07, 982-N08 | Progress reports exist for the first two forms. Their complete refutations were unavailable in the recovered corpus. The entries remain PARTIAL, PARTIAL and OPEN. |
| 982-R06 | Two selected grid pins in one sector can both witness the same target pair. For odd \(M\ge11\) let \(h=\pi/M,c=\cos h,s=\sin h,u=s^2/32\). Use pins \((c,\pm s)\) and targets \((c\pm u,s/2)\). The two diagonals meet internally. Both targets have arguments in \((-h,h)\) since \(c-u>c/2\). The deviation from squared radius \(c^2\) is \(s^2/4\pm2cu+u^2\), positive and less than \(s^2/3\), whereas \(c^2\tan^2(2h)>s^2/3\). Their bisector is \(x=c\). This refutes the local same-sector implication. The repaired threshold relies on a separate concurrence argument. |
| 982-A03, 982-A04 | The local exact 30-point enumeration checked all 4,060 oriented triples and found a unique metric proportional to \((2,1,2)\) with a collision at every pin. The two starting pins gave candidate counts 45,555 and 53,951. The one surviving metric gave six pins with 15 and 24 with 28 distances. For each event line of either starting pin another pin was found that did not have that event line. Thus the projective intersections cover all metrics with collisions everywhere. The separately reported 58,649 candidates use an original coordinate file still unavailable. |
| RUP and Lean paths | The independent LRAT check requires the upstream comment-line verdict. Sparse LRAT additions failed Lean for the 927-step refutation, and dense reindexing passed the real trace. The checker accepted a small contradictory formula and rejected the same proof on a satisfiable formula. Solver success alone has no certification status. |
| 982-J01–J06 | The source derivation uses actual Jacobian rows. Transcendence degree alone cannot bound tangent dimension at a singular configuration. The block-rank hypotheses, density extremizers and fixed-field claim remain in the current review queue. |
| 982-T01 | The original C++ source was rebuilt and returned zero surviving candidates at 4 through 9 in the strict-norm mode, including 4,376 nodes at 8 and 11,516 at 9. The Euclidean supplementary mode reproduced all six archived counts and zero survivors. The norm proof uses crossing inequalities and abstract equality partitions. An exact \(\ell_4\) example in the original audit rules out simply carrying over the Euclidean diameter-cap lemma. |

## Remaining review

Some P1/P2 results have substantial original proofs and prior reviews, including high two-circle cover, odd grid repairs, and Jacobian rigidity. Their DRAFT entries identify the proof material and the dependency. First-pass line-by-line adjudication and detailed priority comparison remain open for those entries. Authorship of the manuscript and redistribution terms for raw proof bundles need human approval before public release.
