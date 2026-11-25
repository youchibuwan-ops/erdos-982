"""Exact arithmetic for the revised general-bound proof (982-G05)."""

from fractions import Fraction as Q
from math import isqrt

import sympy as sp


D = Q(353, 40000)
ETA = Q(3, 1667)
X_CUT = Q(3, 50)
X_MAX = Q(7, 100)
ROOT_SCALE = 10**8


def verify(condition, name):
    if not condition:
        raise ArithmeticError(name)


def root_interval(value):
    verify(value >= 0, "negative radicand")
    scaled = isqrt(int(value * ROOT_SCALE**2))
    lower = Q(scaled, ROOT_SCALE)
    upper = Q(scaled + 1, ROOT_SCALE)
    verify(lower**2 <= value < upper**2, "square-root enclosure")
    return lower, upper


def check_polynomials():
    x, w, s = sp.symbols("x w s")
    rho = sp.Rational(1, 3) - x
    delta = ETA - sp.Rational(3, 8) * x**2
    u = 16 * D**2 + 8 * delta
    v = 16 * D**2 + sp.Rational(24, 5) * delta

    def positive_quadratic(expression):
        a, b, c = sp.Poly(expression, x).all_coeffs()
        return a > 0 and 4*a*c > b*b

    verify(Q(8, 3) * ETA < X_MAX**2, "x domain")
    verify(rho.subs(x, X_MAX) > 11*D, "positive side for A+")
    verify(positive_quadratic((rho - 11*D)**2 - sp.Rational(9, 5)*u
                             - sp.Rational(9, 4)*v), "A+")
    verify(positive_quadratic((rho - 6*D)**2 - 4*u), "OV")

    def positive_on(expression, left, right):
        poly = sp.Poly(expression, x)
        return poly.eval(left) > 0 and poly.count_roots(left, right) == 0

    verify(rho.subs(x, X_MAX) > 12*D, "positive side for no overlap")
    verify(positive_on((rho - 12*D)**2 - 4*u, X_CUT, X_MAX),
           "no overlap for x >= 3/50")
    endpoint = 6*s + w
    overlap = 2*endpoint - rho
    B = 72*endpoint*s - 396*s*s - 12*(endpoint-5*s)*overlap - 23*overlap**2
    derivative = sp.expand(w*sp.diff(B, s) + 16*s*sp.diff(B, w))
    identity = -4*(4800*s*s + 2638*s*w + 300*w*w - 416*rho*s - 141*rho*w)
    verify(sp.expand(derivative - identity) == 0, "endpoint derivative")
    reduced = sp.Poly(sp.rem(B.subs(s, D), w*w-u, w), w)
    p = reduced.nth(0)
    q = reduced.nth(1)
    verify(q.subs(x, X_CUT) > 0 and sp.diff(q, x) < 0, "coefficient of w")
    verify(positive_on(q*q*u-p*p, 0, X_CUT), "positive endpoint B")
    integral_margin = D/2 - 9*D*D - ETA
    verify(integral_margin > 0 and integral_margin**2 > 3*D*D*(16*D*D + 8*ETA),
           "integral estimate")


def check_overlap_boxes():
    active = 0
    minimum = Q(1)
    for i in range(384):
        left = D * i / 384
        right = D * (i+1) / 384
        rhs = 4*left + 3*root_interval(16*left*left + Q(8, 3)*ETA)[0]
        for j in range(768):
            lower_x = X_CUT*j/768
            upper_x = X_CUT*(j+1)/768
            max_delta = ETA - Q(3, 8)*lower_x**2
            min_rho = Q(1, 3) - upper_x
            max_U = 6*right + root_interval(16*right*right + 8*max_delta)[1]
            if 2*max_U <= min_rho:
                continue
            min_cutoff = min_rho - max_U
            a_third = 5*right + root_interval(16*right*right + Q(8, 3)*max_delta)[1]
            verify(min_cutoff > 9*right and min_cutoff > a_third, "monotonicity domain")
            min_cost = (min_cutoff-right)*(min_cutoff-9*right)/8
            max_leftover = max(Q(0), max_delta-min_cost)
            lhs = min_cutoff + 2*root_interval(16*right*right + 4*max_leftover)[1]
            margin = rhs-lhs
            verify(margin > 0, f"overlap inequality in rectangle {i}, {j}")
            minimum = min(margin, minimum)
            active += 1
    return active, minimum


if __name__ == "__main__":
    check_polynomials()
    count, margin = check_overlap_boxes()
    print(f"982-G05 exact parameter inequalities verified in {count} potentially overlapping boxes.")
    print(f"Smallest certified box margin: {margin} (approximately {float(margin):.7f})")
