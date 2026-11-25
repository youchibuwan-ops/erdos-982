"""Verify the integer octagon in 982-X02 using only exact integer arithmetic."""

from itertools import combinations


POINTS = ((0, 0), (1, -4), (4, -13), (8, -11), (28, 0), (8, 11), (4, 13), (1, 4))


def squared(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2


def orientation(p, q, r):
    return (q[0] - p[0])*(r[1] - p[1]) - (q[1] - p[1])*(r[0] - p[0])


if __name__ == "__main__":
    if not all(orientation(*triple) > 0 for triple in combinations(POINTS, 3)):
        raise ValueError("sample is not in strict convex cyclic order")
    pairs = sorted((squared(p, q), p, q) for p, q in combinations(POINTS, 2))
    if pairs[-1] != (784, POINTS[0], POINTS[4]) or pairs[-2][0] >= 784:
        raise ValueError("expected a unique diameter")
    counts = [len({squared(p, q) for q in POINTS if q != p}) for p in POINTS]
    if counts != [3, 7, 7, 7, 3, 7, 7, 7]:
        raise ValueError(f"unexpected pin counts {counts}")
    print(f"982-X02: strict convexity, unique diameter and pin counts {counts} verified.")
