# Finite support profiles and encoding

The [manuscript](../manuscript.tex) proves the minimum-disk reduction, rank semantics, and the angle budgets for convex caps. This note gives the remaining implications used by the archived formulas.

## Profile coverage

For even \(2h\) the candidate profiles are precisely the positive triples \(a\ge b\ge c\) with sum \(2h\) and \(a<h\). The first seven even sizes from 6 through 18 have respectively \(1,1,2,3,4,5,7\) such profiles. For 18, the six unbalanced profiles each have one formula. For \((6,6,6)\), relabel to \(AB\ge BC\ge CA\) and retain the four combinations of equality and strict inequality between adjacent side lengths.

| Profile | Coverage argument |
| --- | --- |
| \(20:(9,9,2),(9,8,3)\) | One unrestricted side-order formula per profile in either archived version. |
| \(20:(9,7,4)\) | The nine-edge chain at \(AB\) uses all nine rank levels at both ends, making \(AB\) largest or tied. Six weak orders survive. In \(AB>BC>CA\), the seven-edge chain forces rank 6 or 7 for \(BC\) at \(B\). |
| \(20:(9,6,5)\) | With the same maximum side, orders 000, 101, 110 need no split. In 100, 201, 210 the rank of \(C\) at \(B\) is 5, 6, 7. If 210 and rank 6, the rank of \(C\) at \(A\) is 4, 5, 6, 7. For rank 4 the six-edge \(BC\) chain skips exactly one of 0 through 5. |
| \(20:(8,8,4)\) | Relabel \(A,C\) so \(AB\ge BC\). Six of eight weak orders are direct. In 210 the rank of \(C\) at \(B\) is at least seven, so \(A\) has rank eight, giving one omission on \(BA\). In 110 the common rank is seven or eight. At eight swap the chains so the smaller omission is on \(BA\). For smaller omission 0 through 4 the other omission is unrestricted. The rest are the six unordered pairs from 5, 6, 7. |
| \(21:(8,8,5)\) | Relabel \(A,C\) so \(AB\ge BC\). Seven weak orders are direct. In 110 the common rank at \(B\) is seven or eight. For rank eight split on the single rank omitted from \(BA\). The other chain's omissions are unrestricted. |
| \(21:(8,7,6)\) | All thirteen weak orders of the three sides. |
| \(21:(7,7,7)\) | Relabel to order three sides, retaining one strict and two isosceles cases. In the equilateral case each support vertex sees the common side length at rank 6, 7, or 8. Sort the three pin ranks, giving ten multisets. |
| \(22:(8,8,6)\) | Single formula with a nine-distance budget. This excludes fewer than ten distances on the profile. Eleven would be required for the conjecture at 22. |

The weak-order conventions start at zero or one depending on the case. With a prescribed omitted rank \(m\), the \(j\)-th chain distance before the largest has rank \(j-1+\mathbf 1_{\{j-1\ge m\}}\). This condition is written as its two threshold bounds. The geometric symmetries used above concern the freedom to relabel the boundary.

## Disk clauses and angle comparisons

For finer angle bins the floor interpretation uses the generator's supplied resolution. If one angle is at least \(60^\circ\) and a second is strictly larger, the third is strictly smaller. The threshold in the supplement inequality comes from \(V+\gamma\ge\pi\) for a cap angle \(V\) and opposite support angle \(\gamma\). Thus when the threshold \(j\pi/G\) fails at \(\gamma\), its complement holds at \(V\). The right-angle predicate includes the boundary case.

For the prefix clauses, center the support circle at \(O\). Write the arguments of \(A,B,C\) as \(-\delta,\delta,\pi+\varepsilon\) with \(-\delta<\varepsilon<\delta\). Along the \(AB\) chain the argument \(u\) of a cap point \(x\) strictly increases. The prefix predicate is \(u\le\varepsilon\). In this case \(C\) is the unique farthest point of arc \(CA\) from \(x\) by the cosine rule on the arc. This maximum remains unique on the cap by convexity of squared distance. For \(u\ge\varepsilon\) the corresponding result holds on \(BC\), and at equality both deductions hold. The tests \(CA>CB\) iff \(\varepsilon<0\), and \(xB>xA\) iff \(u<0\), give the strict and weak prefix implications. Hence \(xC>xA,xC>xB\) cannot both fail. For equilateral supports \(xC\) exceeds both and, by chain monotonicity, exceeds all other \(AB\)-chain distances.

In disk mode \(Ax\le2R\cos\angle OAx\). If \(Ax\ge AB\), the ray lies within \(\pi/2-\gamma\) of \(AO\). If \(AB\) is at least as long as any other support side, \(\gamma>\pi/4\), since otherwise one more angle would be at most \(\pi/4\), contradicting acuteness. If \(AB\) is longest, \(\gamma\ge\pi/3\), with equality only for an equilateral support triangle. The only way to attain cone separation \(\pi/3\) is the pair \(\{B,C\}\) on its two bounding rays, since those rays meet the disk at length \(AB\). This exception is preserved in the formula.

For radial comparison at cyclically ordered \(p,a,x,b\), let \(\alpha=\angle apx\), \(\beta=\angle xpb\). The ray to \(x\) is between the others and \(\alpha+\beta<\pi\). If \(pa=pb\), then \(xa\le xb\) implies \(\alpha\le\beta\) by the cosine rule. Under \(pa\ge pb\ge px\) the same follows because squared distance is nondecreasing with target radius above \(px\) and strictly increasing with angle. The auxiliary atom may be assigned when either premise holds. If \(\alpha\ge\pi/2,\ pa\ge pb\), then \(xa^2\ge px^2+pa^2>px^2+pb^2-2px\cdot pb\cos\beta=xb^2\). Thus the clauses constrain every real counterexample assigned to them.

A core ID file selects a subset of the rebuilt original formula. The independent driver checks its range and uniqueness, actual formula line count, published hashes when present, and exact proof termination. Unsatisfiability of the subset implies unsatisfiability of the full formula.
