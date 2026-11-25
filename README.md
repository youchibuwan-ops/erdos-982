# Erdős Problem #982: Improved Bounds, Computer-Assisted Proofs, and Structural Results

For \(n\) distinct points in strictly convex position in the Euclidean plane, must some vertex see at least \(\lfloor n/2\rfloor\) distinct distances to the other points? A regular \(n\)-gon attains that target. The unrestricted problem remains open. [Official problem](https://www.erdosproblems.com/982)

- The general lower bound here is \((13/36+1/1667)n-O(1)\), with a revised count of surviving good chords and exact rational parameter verification.
- For planar samples with no three collinear, the bound improves to \(\lceil n/2\rceil\) when the coordinates are rational up to similarity. It also holds over every odd-degree real number field and over a broader class defined by ramification at 2.
- For unrestricted strictly convex polygons the finite results give \(f(n)=\lfloor n/2\rfloor\) at \(3\le n\le19\) and \(n=21\). At \(n=20\) the value is either 9 or 10. The support profiles \((8,7,5),(8,6,6),(7,7,6)\) remain unresolved.
- The structural proofs cover cocircular equality, exact rational cocircular values, conic samples, constant-width boundaries, exceptional affine metrics, and finite samples on several polynomial graphs.

The [English manuscript](manuscript.tex) contains the reviewed arguments. The [finite encoding proof](proofs/finite-encoding.md) connects the geometric conditions to the rebuilt formulas. [Results](RESULTS.md), [certificate replay](certificates/README.md), [Lean](lean/README.md), and [references](REFERENCES.md) give the evidence for each scope and status. The [audit](AUDIT.md) records corrections and unresolved work.

For local verification, start with [reproducibility](REPRODUCIBILITY.md). Raw Chinese-language sources and supplied archives have a [SHA-256 inventory](research_logs/sources.json). The repository is prepared for human review before public release.
