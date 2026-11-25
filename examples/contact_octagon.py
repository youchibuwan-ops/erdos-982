"""Exact minimum-disk contact counterexample in 982-X03."""

from itertools import combinations

from sympy import QQ, Rational as Q, sqrt


def squared_distance(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2


def orientation(p, q, r):
    return (q[0] - p[0])*(r[1] - p[1]) - (q[1] - p[1])*(r[0] - p[0])


def main():
    h = sqrt(3)/2
    half = Q(1, 2)
    a, b, c = (half, 0), (0, h), (-half, 0)
    u, v = (h - half, half), (sqrt(2)/2 - half, sqrt(2)/2)
    p = (a, u, v, b, (-v[0], v[1]), (-u[0], u[1]), c, (0, h-1))
    if not all(orientation(*triple).is_positive for triple in combinations(p, 3)):
        raise ValueError("strict convexity failed")
    center = (0, h/3)
    field = QQ.algebraic_field(sqrt(2), sqrt(3))
    contacts = []
    for index, point in enumerate(p):
        slack = field.from_sympy(Q(1, 3) - squared_distance(point, center))
        if not slack:
            contacts.append(index)
        elif not field.to_sympy(slack).is_positive:
            raise ValueError("point escaped minimum disk")
    counts = [len({field.from_sympy(squared_distance(pin, q)) for q in p if q != pin})
              for pin in p]
    if contacts != [0, 3, 6] or counts != [3, 5, 6, 3, 6, 5, 3, 4]:
        raise ValueError((contacts, counts))
    # The three contacts form an equilateral triangle, so their circle is minimal.
    print(f"982-X03: contact indices {contacts}; distance counts {counts}")


if __name__ == "__main__":
    main()
