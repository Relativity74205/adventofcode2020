import pytest

import puzzle05a


@pytest.mark.parametrize('row_str, expected', [
    ('FBFBBFF', 44),
    ('FFFFFFF', 0),
    ('BBBBBBB', 127),
    ('BFFFBBF', 70),
    ('FFFBBBF', 14),
    ('BBFFBBF', 102),
])
def test_get_row(row_str, expected):
    assert puzzle05a.get_row(row_str) == expected


@pytest.mark.parametrize('row_str, expected', [
    ('RLR', 5),
    ('LLL', 0),
    ('RRR', 7),
    ('RLL', 4),
])
def test_get_col(row_str, expected):
    assert puzzle05a.get_col(row_str) == expected
