import math

import pytest

from citest import mean, median, rms


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
