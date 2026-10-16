import math
import statistics

import pytest

from citest import mean, median, rms, stdev


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


@pytest.mark.parametrize(
    "xs, expected",
    [([3, 1, 2], 2), ([4, 1, 3, 2], 2.5), ([7], 7)],
)
def test_median(xs, expected):
    assert median(xs) == expected


def test_rms():
    assert math.isclose(rms([3, 4]), math.sqrt(12.5))


@pytest.mark.parametrize("fn", [mean, median, rms])
def test_empty_raises(fn):
    with pytest.raises(ValueError):
        fn([])


def test_stdev():
    assert math.isclose(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 2.138089935299395)


def test_stdev_matches_statistics_module():
    xs = [1.5, 2.25, -3.0, 10.0, 0.0]
    assert math.isclose(stdev(xs), statistics.stdev(xs))


@pytest.mark.parametrize("xs", [[], [5]])
def test_stdev_too_few_values(xs):
    with pytest.raises(ValueError):
        stdev(xs)
