# Results register

The [JSON register](results.json) is the source of record. Geometry, numerical replay, Lean checks and priority are tracked per entry. A reviewed result has an independently checked mathematical argument in this repository. Draft status includes claims with substantial earlier review where first-pass adjudication is incomplete.

Here \(d_P(p)\) counts positive distances from pin \(p\), \(D(P)\) is the largest pin count, and \(f(n)\) minimizes that maximum over strictly convex Euclidean \(n\)-point sets.

## 982-A01 — Exceptional affine metrics

At most O(n) positive definite forms modulo scaling on a fixed strictly convex n-point set violate sum_p d_P(p)≥binom(n,2); in particular at most O(n) violate the half bound.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md § Affine metrics

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/affine.tex)

Dependencies — Szemerédi–Trotter theorem · Equality-matrix factorization

## 982-A02 — Forms not defined over the coordinate field

For a strict convex n≥3 point set in K², a real positive definite form with no scalar representative over the real coordinate field K has multiplicity at most two at every pin. Some pin sees at least n−3 distances, or n−2 when n is odd.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/AFFINE_METRICS.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/affine.tex)

Dependencies — Linear independence of rank-one matrix differences

## 982-A03 — Explicit affine 30-point family

In the integer-coordinate family encoded in the cited script the only metric with D(P)<29 is proportional to the matrix with diagonal 2 and off-diagonal 1, where D(P)=28.

**REPRODUCED** · exact integer reproduction passed · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-affine30-recheck.py · workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](AUDIT.md)

Dependencies — Projective enumeration of equal-distance event lines

## 982-A04 — Separate affine 30-point family

The author-reported 58,649 candidates refer to a different 30-point input. The exact original coordinates have not been located.

**MISSING_SOURCE** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md § 30-point comparison

Attribution — Project record; exact author/model uncertain where source is silent.

The locally reproduced 30-point configuration is a separately specified example.

## 982-A05 — Affine 21-point instance

In the source's exact 21-point coordinate example, the identity metric gives 5 distances at the first pin and 20 at all others. Its affine candidate search reports 1,121 distinct positive definite forms, one with the first pin below ten and zero counterexamples.

**REPRODUCED** · archived rational enumeration reproduced: 1,121 candidates, one failing first pin, zero counterexamples · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/affine_example_21.json · AFFINE_METRICS.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

## 982-A06 — Finite affine reduction

For any fixed strictly convex real n≥3 point set, every projective positive definite counterexample metric is among at most binom(n−1,3) candidates from three target vectors equidistant at one chosen pin.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/AFFINE_METRICS.md, final proposition

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/affine.tex)

Dependencies — 982-A02 independence lemma · At least one triple of equal targets at a failing pin

## 982-C01 — Cocircular lower bound

Each pin of m≥2 distinct cocircular points sees at least floor(m/2) distances.

**REPROVED** · none asserted · no end-to-end project proof

Priority assessment — classical elementary consequence.

Source record — workspace/erdos-982-cocircular.md, Theorem 2

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/geometry.tex)

## 982-C02 — Odd cocircular equality

For odd m≥3 simultaneous equality at every pin holds precisely for a regular m-gon.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-cocircular.md, Theorem 2

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/geometry.tex)

## 982-C03 — Even cocircular equality

For even m≥6 equality at all pins characterizes the regular m-gon, regular (m+1)-gon minus one vertex, or regular (m−1)-gon with one vertex’s antipode adjoined.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-cocircular.md, Theorem 2

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/geometry.tex)

Dependencies — 982-C01 · Complex moment identities

## 982-C04 — Even n with n−2 cocircular vertices

For even n≥8, a strict convex n-gon with at least n−2 vertices on one circle has D(P)≥n/2.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-cocircular.md, Theorem 1

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/geometry.tex)

Dependencies — 982-C03 · Circle-axis reflection

## 982-C05 — Odd n with n−3 cocircular vertices

For odd n≥9, a strict convex n-gon with at least n−3 vertices on one circle has D(P)≥floor(n/2).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-cocircular.md, Theorem 1

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/geometry.tex)

Dependencies — 982-C04

## 982-C06 — Exact rational cocircular values

For m≥3 rational cocircular points the minimum of D(P) equals m−1 at m=3,5,6,7 and m−2 at m=4 or m≥8.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-short-arcs-review.md § 6

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/structures.tex)

Dependencies — Roots of unity in Q(i) · Cocircular reflection

## 982-C07 — Eight rational cocircular extremizers

At m=8, the rational cocircular minimizers of D(P) are exactly the unions of two disjoint cocircular rational squares.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-short-arcs-review.md § 6

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/structures.tex)

Dependencies — 982-C06

## 982-C08 — Even circle plus one point

On adding one point neither on the circle nor its center to 2k≥4 cocircular points, some pin sees at least k+1 distances, without convexity.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_3_to_19.zip!/earlier/near_circle.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-C09 — Odd near-cocircular rigidity

For odd n≥5, if a strictly convex n-point set has n−1 cocircular vertices and D(P)=floor(n/2), it is regular.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/NEAR_CIRCLE_RIGIDITY.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-C10 — Explicit cocircular density

For strictly convex P with m points on a circle and t off it, m≥2t+42 implies an on-circle pin reaches floor(n/2).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_3_to_19.zip!/CIRCLE.md · workspace/erdos-982-majority-review.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/majority.tex)

Dependencies — Beukers–Smyth cyclotomic point bound

Statement limited to the strictly convex part proved in the manuscript.

## 982-C11 — Asymptotic strict majority

Every circle in a strictly convex counterexample contains at most n/2+O(n/log(2n)) vertices with an absolute constant.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-majority-review.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/majority.tex)

Dependencies — Evertse–Schlickewei–Schmidt unit equation theorem

## 982-C12 — Two structural majority thresholds

A strict convex set with m vertices on a circle and t off has an on-circle qualifying pin if m≥3t/2+66 and either off-circle vertices are contiguous in boundary order or they are on a smaller concentric circle.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-gpt6pro-analytic-audit.md

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — Beukers–Smyth · Group decomposition

Current source indexed; independent technical adjudication still pending.

## 982-C13 — Finite angular subgroup

If each radial reflection misses at most h partners in an m-point circle set and m>2h, the points lie on a regular polygon of order at most 2^(m−1).

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-circle-order.md

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-C14 — Counterexample angular grid

For a strictly convex sample with m circular and t off-circle points and m≥(1+1/sqrt(2))t+47, if all on-circle pins fail the half bound, the m points lie in a finite regular polygon grid.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-gpt6pro-analytic-audit.md · workspace/erdos-982-circle-order.md

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-C13 · Circle-fiber bounds

Current source indexed; independent technical adjudication still pending.

## 982-D01 — Binary distance separation

An n-point planar set with n ≥ 2, no collinear triples and a separating binary tree has D(P) ≥ ceil(n/2). Each split separates distances from any pin inside its node to targets in opposite children.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-dyadic.md §§ 1–3 · workspace/erdos-982-tree-check.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/dyadic.tex)

Dependencies — Perpendicular bisector pair count · Concavity on a closed interval

## 982-D02 — Rational coordinates

For n ≥ 2 distinct planar points with no three collinear, rational coordinates after a similarity imply D(P) ≥ ceil(n/2).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-dyadic.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/dyadic.tex)

Dependencies — 982-D01 · Integer parity

## 982-D03 — Ramified quadratic extension

The same bound holds for coordinates in a real number field K, up to similarity, when K(i)/K ramifies above 2 at some finite place.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-dyadic.md § Number fields

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/dyadic.tex)

Dependencies — 982-D01 · Norm and residue field of a ramified quadratic local extension

## 982-D04 — Odd-degree fields

The same bound holds for coordinates in any odd-degree real number field, up to similarity.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-dyadic.md § Number fields

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/dyadic.tex)

Dependencies — 982-D03 · Local degree identity

## 982-D05 — Real algebraic transfer

Existence of a strictly convex counterexample at a given size implies existence at the same size over the real algebraic numbers, preserving the orientation and distance comparison signs.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Counterexample conditions

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/dyadic.tex)

Dependencies — Transfer between real closed fields

## 982-D06 — Number-field obstruction

For any real number field K containing the coordinates of a similar copy of a counterexample, all ramification indices above 2 are even and K(i)/K is unramified at every such place. In particular [K:Q] is even.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Counterexample conditions

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/dyadic.tex)

Dependencies — 982-D03 · 982-D04 · Normalized valuation of 1+i

## 982-D07 — Transcendental base

For algebraically independent real u_1,…,u_h and a finite odd-degree real extension K/Q(u_1,…,u_h), general-position K-coordinate samples satisfy D(P) ≥ ceil(n/2).

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Transcendental parameters

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-D03 proof mechanism · Finite integral closure and local degree identity

Current source indexed; independent technical adjudication still pending.

## 982-D08 — Rational squared distances

When all squared distances are rational multiples of one positive scale and the normalized vertical quadratic factor has squarefree d≡1 or 2 mod 4, a set with no collinear triples satisfies D(P) ≥ ceil(n/2).

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Squared distances

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-D01 · Eisenstein at 2

Current source indexed; independent technical adjudication still pending.

## 982-D09 — Cyclotomic real tower

The same bound holds for samples with no collinear triples in the real 2-power cyclotomic tower.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Number fields

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-D03 · Eisenstein for 2-power cyclotomic polynomials

Current source indexed; independent technical adjudication still pending.

## 982-D10 — Tree recognition

Recursively split the graph joining two targets when a third point in the current set sees equal distances. All leaves are singletons exactly when a separating binary tree exists.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Tree test

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-D11 — Sharpness in the tree class

The regular 2^j-gon and the result of deleting one vertex for j≥2 admit separating trees with D(P)=ceil(n/2).

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-dyadic.md § Tree sharpness

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-F01 — Exact values from 3 to 13

For every integer n with 3 ≤ n ≤ 13, f(n)=floor(n/2).

**LITERATURE** · 7/7 required traces replayed with two external checkers · 7/7 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior literature or public work.

Source record — Lee public proof · Quantavane Lean · proof-packs/Erdos982_3_to_19.zip · gemini/成果.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon · Minimum support reduction · Lee computational proof

Classical arguments and Lee precede the current compilation, including Fishburn's octagon result. Quantavane's Lean version is external.

## 982-F02 — Exact values from 14 to 19

For every integer n with 14 ≤ n ≤ 19, f(n)=floor(n/2).

**COMPUTER_ASSISTED** · 19/19 required traces replayed with two external checkers · 19/19 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon · Minimum support reduction · Earlier and n18 RUP traces

## 982-F03 — Exact value at 21

f(21)=10 for strictly convex Euclidean planar sets.

**COMPUTER_ASSISTED** · 71/71 required traces replayed with two external checkers · 71/71 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — proof-packs/Erdos982_round3.zip!/FINITE_REDUCTION.md · workspace/erdos-982-round3-review.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

Dependencies — 982-N01 · 982-N02 · 982-N03 · 982-N04 · 982-N09 · 982-N10 · 982-N11

Uses only the four 9-leading 20-point profiles to pass from 21 to 20. This leaves three different 20-point profiles unresolved.

## 982-F04 — Independent 22-point profile

A strict convex 22-gon with acute minimum-disk support gaps (8,8,6) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/certificates/n22_886.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Minimum support reduction · n22_886 trace

## 982-F05 — Twenty-point global problem

9 ≤ f(20) ≤ 10, with exact value open. The lower bound follows by deleting a vertex and using n=19.

**OPEN** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-cumulative-report-2026-11-25.pdf p.2

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-F02 · Regular 20-gon

## 982-F10 — Exact value at 3

f(3)=1 for strictly convex Euclidean planar point sets.

**LITERATURE** · elementary lower bound without a trace · external sources in 982-F01 for n≤13; end-to-end here pending

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F11 — Exact value at 4

f(4)=2 for strictly convex Euclidean planar point sets.

**LITERATURE** · elementary lower bound without a trace · external sources in 982-F01 for n≤13; end-to-end here pending

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F12 — Exact value at 5

f(5)=2 for strictly convex Euclidean planar point sets.

**LITERATURE** · elementary lower bound without a trace · external sources in 982-F01 for n≤13; end-to-end here pending

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F13 — Exact value at 6

f(6)=3 for strictly convex Euclidean planar point sets.

**LITERATURE** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F14 — Exact value at 7

f(7)=3 for strictly convex Euclidean planar point sets.

**LITERATURE** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F15 — Exact value at 8

f(8)=4 for strictly convex Euclidean planar point sets.

**LITERATURE** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F16 — Exact value at 9

f(9)=4 for strictly convex Euclidean planar point sets.

**LITERATURE** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F17 — Exact value at 10

f(10)=5 for strictly convex Euclidean planar point sets.

**LITERATURE** · 2/2 required traces replayed with two external checkers · 2/2 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F18 — Exact value at 11

f(11)=5 for strictly convex Euclidean planar point sets.

**LITERATURE** · 2/2 required traces replayed with two external checkers · 2/2 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F19 — Exact value at 12

f(12)=6 for strictly convex Euclidean planar point sets.

**LITERATURE** · 3/3 required traces replayed with two external checkers · 3/3 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F20 — Exact value at 13

f(13)=6 for strictly convex Euclidean planar point sets.

**LITERATURE** · 3/3 required traces replayed with two external checkers · 3/3 required traces checked in Lean Std as imported CNFs; external Quantavane end-to-end for n≤13 uses native evaluation

Priority assessment — prior art.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F21 — Exact value at 14

f(14)=7 for strictly convex Euclidean planar point sets.

**COMPUTER_ASSISTED** · 4/4 required traces replayed with two external checkers · 4/4 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; finite literature comparison in REFERENCES.md.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F22 — Exact value at 15

f(15)=7 for strictly convex Euclidean planar point sets.

**COMPUTER_ASSISTED** · 4/4 required traces replayed with two external checkers · 4/4 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; finite literature comparison in REFERENCES.md.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F23 — Exact value at 16

f(16)=8 for strictly convex Euclidean planar point sets.

**COMPUTER_ASSISTED** · 5/5 required traces replayed with two external checkers · 5/5 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; finite literature comparison in REFERENCES.md.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F24 — Exact value at 17

f(17)=8 for strictly convex Euclidean planar point sets.

**COMPUTER_ASSISTED** · 5/5 required traces replayed with two external checkers · 5/5 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; finite literature comparison in REFERENCES.md.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-F25 — Exact value at 18

f(18)=9 for strictly convex Euclidean planar point sets.

**COMPUTER_ASSISTED** · 10/10 required traces replayed with two external checkers · 10/10 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; finite literature comparison in REFERENCES.md.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Minimum enclosing disk and support profiles

## 982-F26 — Exact value at 19

f(19)=9 for strictly convex Euclidean planar point sets.

**COMPUTER_ASSISTED** · 10/10 required traces replayed with two external checkers · 10/10 required traces checked in Lean Std as imported CNFs

Priority assessment — candidate contribution; finite literature comparison in REFERENCES.md.

Source record — proof-packs/Erdos982_3_to_19.zip!/README.md · workspace/erdos-982-gpt6pro-finite-audit.md

Attribution — Published and archived sources as recorded in 982-F01 and 982-F02..

[Proof or audit](proofs/finite-encoding.md)

Dependencies — Regular polygon upper bound · Delete one vertex and use the preceding even result

## 982-G01 — Moser bound

For strictly convex n-point sets, D(P) ≥ ceil(n/3).

**LITERATURE** · none asserted · no end-to-end project proof

Priority assessment — prior literature or public work.

Source record — Moser 1952

Attribution — Named public sources.

## 982-G02 — Erdős–Fishburn bound

For strictly convex n-point sets with n ≥ 4, D(P) ≥ floor(n/3)+1.

**LITERATURE** · none asserted · no end-to-end project proof

Priority assessment — prior literature or public work.

Source record — Erdős–Fishburn, Postscript

Attribution — Named public sources.

## 982-G03 — Dumitrescu bound

For strictly convex n-point sets, D(P) ≥ ceil((13n−6)/36).

**LITERATURE** · none asserted · no end-to-end project proof

Priority assessment — prior literature or public work.

Source record — Dumitrescu 2006

Attribution — Named public sources.

## 982-G04 — Published cap refinement

For strictly convex n-point sets, D(P)≥(13/36+1/22701)n−O(1), with an absolute additive constant.

**LITERATURE** · none asserted · no end-to-end project proof

Priority assessment — prior literature or public work.

Source record — Nivasch–Pach–Pinchasi–Zerbib 2013

Attribution — Named public sources.

## 982-G05 — Overlapping-window improvement

For every strictly convex n-point planar set, D(P) ≥ (13/36+1/1667)n−C for an absolute C.

**REVIEWED** · exact arithmetic verified · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-carbon-audit.md § General-bound repair · gemini/general_and_cocircular_theorems.md, Theorem A · workspace/erdos-982-general-bound.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/general-bound.tex)

Dependencies — 982-G04 · 982-G08 · NPPZ Lemma 12 · Exact parameter verifier

Uses two corrected stopping-window arguments and an exact arithmetic enclosure. Latest version replaces 982-G06 and 982-G07 as the headline bound.

## 982-G06 — Earlier disjoint-window improvement

For strictly convex planar n-point sets, D(P) ≥ (13/36+1/1740)n−O(1).

**SUPERSEDED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-general-bound.md

Attribution — Project record; exact author/model uncertain where source is silent.

Disjoint-window parameter set retained as proof history.

## 982-G07 — First repaired overlapping-window improvement

For strictly convex planar n-point sets, D(P) ≥ (13/36+1/1674)n−O(1).

**SUPERSEDED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini/general_and_cocircular_theorems.md, Theorem A · workspace/erdos-982-carbon-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

Original positive-part function and early/late comparison needed correction. See AUDIT.md.

## 982-G08 — Kominers preprint bound

For strictly convex n-point sets, D(P)≥(13/36+3/5270)n−O(1), with an absolute additive constant.

**LITERATURE** · none asserted · no end-to-end project proof

Priority assessment — prior literature or public work.

Source record — Kominers 2026, Theorem 1

Attribution — Named public sources.

## 982-J01 — Transcendence-degree bound

For n≥3 distinct planar points with no three collinear, with s qualifying pins, trdeg_Q Q(P)≤2s+576 H_{n−s}.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-block-rank-review.md · workspace/erdos-982-progress-2026-11-25.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/rigidity.tex)

Dependencies — Dvir–Garg–Oliveira–Solymosi block rank

## 982-J02 — True isosceles Jacobian kernel

For n≥3 distinct planar points with no three collinear, the real kernel of the Jacobian of all true equal-distance equations has dimension at most 2s+576 H_{n−s}, where s counts qualifying pins.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-progress-2026-11-25.md § Rank consequence

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/rigidity.tex)

Dependencies — Block rank at the actual configuration

A transcendence-degree bound alone does not bound the kernel of an equal-distance Jacobian at a specialized real configuration.

## 982-J03 — Algebraic local rigidity

For n≥3 distinct planar points with no three collinear and t=dim ker J, one can fix t scalar coordinates from the configuration to give local uniqueness. Over the field F generated by the fixed values, [F(P):F]≤2^(2n−t).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-progress-2026-11-25.md § Rank consequence

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/rigidity.tex)

Dependencies — 982-J02 · Inverse function theorem · Affine Bézout

Local uniqueness is around the actual configuration, after fixing chosen scalar coordinates.

## 982-J04 — Sharp asymptotic parameter density

When trdeg_Q Q(P)/n tends to α>0 for strict convex samples, the claimed optimal liminf D(P)/n is (1+α)/2 for α≤1/2, 1−(1−α)^2 for 1/2≤α≤1, and 1 for 1≤α≤2.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-block-rank-review.md §§ 2–4

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-J01 · Quadratic-residue constructions

Current source indexed; independent technical adjudication still pending.

## 982-J05 — Finite very high parameter density

If trdeg_Q Q(P)≥(1+ε)n, some pin sees at least n−1−48/ε distances.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-block-rank-review.md § 3

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-J01 and slope rank variants

Current source indexed; independent technical adjudication still pending.

## 982-J06 — Bounded-transcendence common-field structure

For a strict convex counterexample there is a subfield of transcendence degree at most 1872 containing the coordinates of more than 16n/17 vertices; each remaining vertex lies on a line over that field through a single common known point.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-block-rank-review.md §§ 5–6

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — Block and scalar rank bounds

Current source indexed; independent technical adjudication still pending.

## 982-M01 — Two circles cover 99 percent

For sufficiently large strictly convex planar n-point sets with at least 0.99n points on two circles, at least n/10 pins attain floor(n/2), uniformly in the circles.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-two-circles.md §§ 7–9

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/two-circles.tex)

Dependencies — Two-circle equal-distance incidence theorem · Cocircular density and concentric-ring estimates

## 982-M02 — Two nonconcentric rings with linear slack

For sufficiently large strictly convex n-point sets partitioned into two nonconcentric circles with at least n/4 points in either part, at least n/2000 pins see more than (1/2+10^−4)n distances.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-short-arcs-review.md § 7 · workspace/erdos-982-two-circles.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/two-circles.tex)

Dependencies — Solymosi–Zahl Theorem 1.4 · Cross-circle non-additivity

## 982-M03 — Two complete concentric regular polygons

If the union of two concentric regular polygons of orders at least three is strictly convex, some pin sees at least floor(n/2) distances for any angle and radii.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_3_to_19.zip!/TWO_RINGS.md · workspace/erdos-982-gpt6pro-analytic-audit.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/two-circles.tex)

Dependencies — Strict convexity constraints on two concentric layers · Beukers–Smyth

The complete two-ring theorem requires strict convexity.

## 982-M04 — Algebraic separation of concentric layers

For points on two concentric circles, if the radius ratio has algebraic degree greater than two over the field generated by the cosines of all direction differences, each pin reaches floor(n/2).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-gpt6pro-analytic-audit.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/two-circles.tex)

Dependencies — See referenced source; dependency audit pending

## 982-M05 — Even grid annulus

At most one point on each of 2h equally spaced rays, h≥4, with radii in (cos(pi/h),1], implies a pin seeing each distance at most twice.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-two-circles.md § 4

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-M06 — Thin annulus sharp radial ratio

For n≥3 points on distinct rays with minimum angular gap δ>0 and radii in [a,b], 0<a≤b, the condition b/a<sqrt(3+cos²δ)−cosδ makes distances strictly increasing on each angular half-sequence at every pin. The ratio is sharp for absence of triple multiplicity at all pins for δ≤π/2.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/SHARP_ANNULUS.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/structures.tex)

Dependencies — Cosine rule and endpoint minimization

## 982-M07 — Short arc plus reflections

For the two specified short arcs and their optional mirrored sample from the unique-diameter construction, at least Ω(n^(4/5)) upper pins distinguish n−O(n^(4/5)) distances.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-short-arcs-review.md

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-N01 — Twenty-point profile (9,9,2)

A strict convex 20-gon with an acute minimum-disk support triple of gaps (9,9,2) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-n20 · proof-packs/Erdos982_round3.zip!/certificates/n20_992_983.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N02 — Twenty-point profile (9,8,3)

A strict convex 20-gon with an acute minimum-disk support triple of gaps (9,8,3) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 1/1 required traces replayed with two external checkers · 1/1 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-n20 · proof-packs/Erdos982_round3.zip!/certificates/n20_992_983.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N03 — Twenty-point profile (9,7,4)

A strict convex 20-gon with an acute minimum-disk support triple of gaps (9,7,4) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 7/7 required traces replayed with two external checkers · 7/7 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/certificates/n20_974.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N04 — Twenty-point profile (9,6,5)

A strict convex 20-gon with an acute minimum-disk support triple of gaps (9,6,5) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 20/20 required traces replayed with two external checkers · 20/20 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/certificates/n20_965.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N05 — Twenty-point profile (8,8,4)

A strict convex 20-gon with an acute minimum-disk support triple of gaps (8,8,4) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 26/26 required traces replayed with two external checkers · 26/26 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — gemini/n20_884_cert · workspace/erdos-982-884-local-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N06 — Twenty-point profile (8,7,5)

The desired exclusion has incomplete author-reported coverage. Order 210 includes unresolved 210_85, 210_86, 210_87 subbranches.

**PARTIAL** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini-progress attachment · workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md

Attribution — Gemini source as recorded; local audit credit is separate.

No complete retained proof for this profile. The progress attachment is a report, not a certificate.

## 982-N07 — Twenty-point profile (8,6,6)

The desired exclusion has incomplete author-reported coverage, 3 of 8 side orders.

**PARTIAL** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini-progress attachment

Attribution — Gemini source as recorded; local audit credit is separate.

No complete retained proof for this profile.

## 982-N08 — Twenty-point profile (7,7,6)

Exclusion of every strict convex counterexample with this support profile remains open in the audited corpus.

**OPEN** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini-progress attachment

Attribution — Gemini source as recorded; local audit credit is separate.

## 982-N09 — Twenty-one-point profile (8,8,5)

A strict convex 21-gon with acute support gaps (8,8,5) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 16/16 required traces replayed with two external checkers · 16/16 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/certificates/n21_885_seven.zip and n21_885_isosceles.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N10 — Twenty-one-point profile (8,7,6)

A strict convex 21-gon with acute support gaps (8,7,6) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 13/13 required traces replayed with two external checkers · 13/13 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/certificates/n21_876.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-N11 — Twenty-one-point profile (7,7,7)

A strict convex 21-gon with acute support gaps (7,7,7) has D(P) ≥ 10.

**COMPUTER_ASSISTED** · 13/13 required traces replayed with two external checkers · 13/13 required traces checked in Lean Std as imported CNFs

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/certificates/n21_777.zip

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/finite-encoding.md)

## 982-O01 — Unrestricted conjecture

Every strictly convex planar n-point set satisfies D(P)≥floor(n/2).

**OPEN** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — Erdős Problem #982

Attribution — Project record; exact author/model uncertain where source is silent.

## 982-O02 — Fishburn sum conjecture

Every strictly convex planar n-point set satisfies sum_p d_P(p)≥binom(n,2).

**OPEN** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — Fishburn, Distances in Convex Polygons

Attribution — Project record; exact author/model uncertain where source is silent.

## 982-P01 — Single polynomial curve curvature bound

For n points on a degree-at-most-d real polynomial parameter curve whose image is not in a line, D(P)≥n−1−O_d(n^(5/7)). The noncircular nonsingular real conic version has an absolute constant.

**LITERATURE** · none asserted · no end-to-end project proof

Priority assessment — prior literature or public work.

Source record — Public CURVATURE.md at 8fda4f2 · workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md

Attribution — Named public sources.

Dependencies — Solymosi–Zahl Theorem 1.4 · Curvature test

The principal bound overlaps the 24 November public manuscript.

## 982-P02 — Exceptional pins on one curve

Under the preceding assumptions only O_{d,ε}(sqrt(n)) pins miss at least εn distances for each fixed ε>0.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — Solymosi–Zahl unbalanced real-grid estimate

Current source indexed; independent technical adjudication still pending.

## 982-P03 — Several polynomial graphs

For n distinct points on r graphs in common orthonormal coordinates with 2≤degree≤d, D(P)≥n−1−C_d r^(9/7)n^(5/7).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — candidate contribution; no equivalent located in reviewed sources.

Source record — workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md §§ 1–3

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/polynomial-graphs.tex)

Dependencies — Solymosi–Zahl Theorem 1.4 · Eisenstein criterion · Analytic implicit function theorem

## 982-P04 — Off-axis distances to affine regular vertices

For m points of the noncircular affine image of one regular polygon, any pin off both ellipse axes sees at least m−44 positive distances.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/ELLIPTIC_DISTANCES.md, Theorem 1

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — Beukers–Smyth §4.1

Current source indexed; independent technical adjudication still pending.

## 982-P05 — Several affine regular ellipses

Take m distinct targets on k noncircular ellipses, each a subset of an affine regular polygon on that ellipse. For pairwise distinct focal separations, or concentric ellipses with pairwise distinct semiaxis pairs, any pin off all 2k axes sees at least m−44k−176 binom(k,2) positive distances.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/ELLIPTIC_DISTANCES.md, Theorem 2

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — 982-P04 · Beukers–Smyth §4.1

Current source indexed; independent technical adjudication still pending.

## 982-R01 — Complete regular core at half density

A strict convex n-point set containing all vertices of a regular m-gon, m≥3 and n≤2m+1, has D(P)≥floor(n/2).

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/REGULAR_CORE.md · workspace/erdos-982-regular-core.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-R02 — Regular core with preserved sides

A complete regular even m≥34 core with four original hull edges, or odd m≥41 core with five original hull edges, gives the half bound regardless of n.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-regular-core.md § Preserved sides

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-R03 — Complete regular core below half

For large n, a complete regular core with m≥n/3+Cn/log n gives the half bound for an absolute C.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/THIRD_DENSITY.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-R04 — One short of half

For a strict convex n-gon containing a full regular m-gon with m=floor(n/2)−1≥500, the half bound holds.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/ONE_SHORT.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-R05 — Bounded-gap incomplete grid

For fixed Q and large n, a subset of m≥n/3+C_Q n/log n regular-grid vertices with consecutive gaps at most Q suffices if at least ceil(log n)^2 vertices are off every original symmetry axis.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/INCOMPLETE_GRID.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-R06 — Odd grid same-sector witness cap

For odd M≥11, two off-circle targets in the same sector of a regular M-grid thin annulus need not have at most one equidistant selected grid pin. The claimed universal local implication is false.

**REFUTED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini/general_and_cocircular_theorems.md, Theorem B proof · workspace/erdos-982-carbon-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

[Proof or audit](AUDIT.md)

Dependencies — Exact four-point witness in AUDIT.md

The exact four-point counterexample invalidates the cited local step, not the separately repaired threshold.

## 982-R07 — Repaired odd thin-grid threshold

For odd M≥11, a strictly convex union of m selected unit M-grid vertices and t points in cos(h)<r≤cos(h)/cos(2h), h=π/M, attains the half bound when m≥3t/2+83/2.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — uses Heineken concurrence; distance threshold is a candidate contribution.

Source record — workspace/erdos-982-carbon-audit.md § Odd regular core

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/odd-grid.tex)

Dependencies — Three-chord concurrence restriction · Beukers–Smyth

R07 uses the repaired triangle-free argument, with no reliance on the refuted same-sector claim.

## 982-R08 — Odd-grid second-circle threshold

With a unit odd-grid core of m points and t off-circle points on one other circle, m≥t+44 suffices in the strict convex setting.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — uses Heineken concurrence; distance threshold is a candidate contribution.

Source record — workspace/erdos-982-carbon-audit.md § Further odd-grid theorem

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/odd-grid.tex)

Dependencies — Beukers–Smyth · Circle-circle bisector count

## 982-R09 — Separated-sector bisector bound

In the odd-grid thin annulus of 982-R07, pairs at cyclic sector separation at least four have at most one equidistant grid pin.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini/general_and_cocircular_theorems.md, Theorem B part 1

Attribution — Gemini source as recorded; local audit credit is separate.

Dependencies — Exact Sturm verification

Current source indexed; independent technical adjudication still pending.

## 982-S01 — Samples of centrally symmetric strict bodies

For a finite sample of a centrally symmetric strictly convex planar boundary, every point farthest from the center sees each distance at most twice.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982.md · proof-packs/Erdos982_round3.zip!/CONICS.md

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/geometry.tex)

Dependencies — Minimum enclosing diameter cap lemma

## 982-S02 — Conic samples

Every strictly convex planar sample of a nondegenerate real conic has a pin with multiplicity at most two for each positive distance.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — independent reproof; overlaps the public November 24 conic manuscript.

Source record — proof-packs/Erdos982_round3.zip!/CONICS.md · pinned public conic manuscript

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

[Proof or audit](proofs/geometry.tex)

Dependencies — 982-S01 · Secant slope monotonicity

The conic statement overlaps the pinned public conic manuscript.

## 982-S03 — Constant-width samples

On a planar constant-width boundary, at least n/2 pins for even n≥4 and ceil(2n/3) pins for odd n≥3 reach floor(n/2).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-constant-width.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/structures.tex)

Dependencies — Supporting faces of constant width · Unimodal edge-bisector count

## 982-S04 — Smooth constant-width pins

On a planar constant-width boundary, every sample pin with a unique supporting line sees at most two occurrences of any positive distance.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-constant-width.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/structures.tex)

Dependencies — Unique supporting line · Constant-width normal chord

## 982-S05 — Exact minimum for unimodal polygons

Among strictly convex n≥3 polygons whose boundary distances are unimodal at every pin, min sum_p d_P(p)=binom(n,2).

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-constant-width.md · workspace/erdos-982-carbon-audit.md

Attribution — Project record; exact author/model uncertain where source is silent.

Dependencies — 982-S03 counting lemma · Two-ring exact counts

Current source indexed; independent technical adjudication still pending.

## 982-S06 — Centrally symmetric bodies with flat edges

For a finite planar sample of a centrally symmetric convex body boundary, some pin sees each positive distance at most twice; collinear samples are allowed.

**DRAFT** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_round3.zip!/CONICS.md, Theorem 1 extension

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

Current source indexed; independent technical adjudication still pending.

## 982-T01 — Strictly convex norm at n≤9

For n from 3 to 9 in strict convex position under any strictly convex planar norm, some pin has at least floor(n/2) distinct norm distances.

**COMPUTER_ASSISTED** · local exact four-point DAG enumeration reproduced for 4 through 9 · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini/成果.md, Theorem 3 · workspace/erdos-982-carbon-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

[Proof or audit](proofs/norms.tex)

Dependencies — See referenced source; dependency audit pending

Original strict norm DAG proof reproduced; the geometry and algorithm are not formalized in Lean.

## 982-T02 — Strictly convex norm universal lower bound

For n≥4 points in strict convex position and any strictly convex planar norm, D(P)≥floor(n/3)+1.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-carbon-audit.md § Norms

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/norms.tex)

Dependencies — See referenced source; dependency audit pending

## 982-T03 — One strictly convex norm circle

For a sample on any circle of a strictly convex planar norm, every pin sees at least floor(n/2) positive norm distances.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — direct consequence of the classical intersection theorem for norm circles.

Source record — gemini/成果.md, Theorem 2 · workspace/erdos-982-carbon-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

[Proof or audit](proofs/norms.tex)

Dependencies — Intersection bound for two homothetic strictly convex norm circles

## 982-X01 — Unique-diameter endpoint extremum

For a strictly convex n≥3 polygon with unique diameter AB, and s≥t vertices on the two sides, d(A)+d(B)≥s+3 and each pair u,v≥2 with u+v=s+3 occurs. The sharp minimum of the better count is ceil(n/4)+1.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-diameter.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/structures.tex)

## 982-X02 — Unique diameter forces a qualifying endpoint

A strictly convex integer octagon with diameter endpoints (0,0),(28,0) and others (1,±4),(4,±13),(8,±11) has d(A)=d(B)=3<4.

**REFUTED** · exact integer reproduction passed · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-diameter.md

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](examples/diameter_octagon.py)

Dependencies — Exact integer coordinate verification

## 982-X03 — Minimum-disk contact strategy fails

A strictly convex octagon has exactly three minimum-disk contact vertices, all seeing three distances, below the target of four.

**REFUTED** · exact radical-coordinate construction verified · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — gemini/成果.md, Theorem 4A · workspace/erdos-982-carbon-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

[Proof or audit](examples/contact_octagon.py)

Dependencies — See referenced source; dependency audit pending

Refutes a contact-only strategy, not the half-distance conjecture.

## 982-X04 — Even average can be below half

For n=4s+2, s≥1, the stated interlaced regular polygons have exactly n/2 pins with n/2 distances and the rest with n/2−1. The sum equals binom(n,2).

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — explicit prior overlap for the first member.

Source record — gemini/成果.md, Theorem 4B · workspace/erdos-982-carbon-audit.md

Attribution — Gemini source as recorded; local audit credit is separate.

[Proof or audit](proofs/structures.tex)

Dependencies — See referenced source; dependency audit pending

The s=1 case is already present in Saller's public note. Infinite-family priority remains under review.

## 982-X05 — Exact 18-point near-counterexample

The two-ring 18-point algebraic example gives eight distances at outer pins and nine at inner pins.

**REPRODUCED** · original exact construction rerun · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_3_to_19.zip!/example/check_near_example.py

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

## 982-X06 — Abstract 18-point obstacle

The supplied abstract metric has eight distances at every point while satisfying the triangle, quadrilateral crossing and three support-chain order constraints used in its control.

**REPRODUCED** · original exact construction rerun · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — proof-packs/Erdos982_3_to_19.zip!/earlier/barrier.py

Attribution — GPT-6 Pro source bundles as identified by contemporaneous audit; registry revisions are separate.

Dependencies — See referenced source; dependency audit pending

X06 is an abstract metric; geometric realizability is not asserted.

## 982-X07 — Multiplicity balance

At a pin with s singleton lengths and e=sum_{k≥3}(k−2) over multiplicity classes, 2d_P(p)=n−1+s−e. The half bound holds exactly when s≥e.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982.md § Repeats

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/affine.tex)

Dependencies — Multiplicity count

## 982-X08 — Double-witness excess in a counterexample

For a strict convex counterexample let e_j count pairs with j bisector witnesses. Then e_2−e_0≥3n/2 for even n and ≥3n for odd n.

**REVIEWED** · none asserted · no end-to-end project proof

Priority assessment — claim-specific priority not established.

Source record — workspace/erdos-982-6pro-gemini-synthesis-2026-11-25.md § Witness count

Attribution — Project record; exact author/model uncertain where source is silent.

[Proof or audit](proofs/affine.tex)

Dependencies — 982-X07 context · Isosceles count by bases and apices
