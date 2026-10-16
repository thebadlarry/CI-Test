"""Small statistics helpers."""

import math
from collections.abc import Sequence


def mean(xs: Sequence[float]) -> float:
    """Arithmetic mean. Raises ValueError on an empty sequence."""
    if not xs:
        raise ValueError("mean() of an empty sequence")
    return sum(xs) / len(xs)


def median(xs: Sequence[float]) -> float:
    """Median (average of the two middle values for an even count)."""
    if not xs:
        raise ValueError("median() of an empty sequence")
    s = sorted(xs)
    mid = len(s) // 2
    if len(s) % 2:
        return float(s[mid])
    return (s[mid - 1] + s[mid]) / 2


def rms(xs: Sequence[float]) -> float:
    """Root mean square."""
    return math.sqrt(mean([x * x for x in xs]))


def stdev(xs: Sequence[float]) -> float:
    """Sample standard deviation (divides by n - 1). Needs at least two values."""
    if len(xs) < 2:
        raise ValueError("stdev() needs at least two values")
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
