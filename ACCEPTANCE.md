# First release review

## Results ready for scientific review

- The general lower bound \((13/36+1/1667)n-O(1)\), with a corrected window argument and a separately reimplemented exact parameter check. All 51,599 potentially overlapping rectangles passed. The coefficient exceeds Kominers's July preprint by \(269/8785090\).
- The \(\lceil n/2\rceil\) bound for rational coordinates up to similarity, for odd-degree real number fields, and for fields admitting the stated ramified quadratic extension. The proof uses no convexity beyond the required absence of collinear triples.
- The exact finite values at \(3\le n\le19\) and \(n=21\), with five separate 20-point support-profile exclusions. The 22-point \((8,8,6)\) archive proves the weaker ten-distance statement independently.
- The reviewed structural results in the manuscript, including cocircular equality and exact rational cocircular values, conic and constant-width samples, high two-circle coverage, several polynomial graphs, actual-Jacobian rigidity, exceptional affine metrics, and the unique-diameter endpoint extremum.

The strongest candidates for distinct contributions in the reviewed literature search include the new unrestricted coefficient, the dyadic pinned bound and number-field criterion, the extra finite cases beyond the known public 13-point interval, and several structural statements. The existing conic manuscript, the already established small cases, and the one-curve curvature theorem have direct public overlap. Claim-by-claim credit and limits appear in [results](RESULTS.md) and [references](REFERENCES.md).

## Reproduction and formalization

DRAT-trim in RUP-only mode and the independent LRAT checker passed all 126 supplied traces. The canonical 124 branches contain 6,159,713 supplied additions. Including two historical alternatives yields 6,466,271 additions across 125 full CNFs. Lean Std checked all 126 imported CNFs, including the historical alternatives. The three Lean profile enumerations use no axioms. The original geometry-to-CNF argument remains a conventional proof in this repository. Quantavane's external end-to-end result reaches 13 and uses disclosed native computation. The exact arithmetic, example controls, and English LaTeX manuscript were built locally.

## Remaining checks and publication

The unrestricted problem, the exact value at 20, the three open or partial 20-point profiles, and the full eleven-distance target at 22 remain open in this corpus. Among the registered proof drafts, several fine regular-core thresholds and the strongest rank-density and common-field refinements still require detailed adjudication. The original alternate 30-point construction lacks its exact coordinate file. The two-circle results have no explicit minimum size. The scholarly priority review is provisional.

The maintainer approved publication of the curated repository on 26 November 2026. The public-source verification workflow is configured for pushes and pull requests. The raw source bundles remain at their original locations with indexed hashes and are excluded from this release. The repository license covers original repository content within the contributors' rights.
