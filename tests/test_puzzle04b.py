import pytest

import puzzle04b


@pytest.mark.parametrize('hcl, expected', [
    ('#000000', True),
    ('#ffffff', True),
    ('#FFFFFF', False),
    ('asd', False),
    ('000000', False),
])
def test_check_hcl(hcl, expected):
    assert puzzle04b.check_hcl(hcl) == expected


@pytest.mark.parametrize('pid, expected', [
    ('#000000', False),
    ('000000000', True),
    ('999999999', True),
    ('00000000', False),
    ('9999999999', False),
    ('00000000a', False),
])
def test_check_pid(pid, expected):
    assert puzzle04b.check_pid(pid) == expected


@pytest.mark.parametrize('val, low, high, expected', [
    ('-1', 0, 2, False),
    ('0', 0, 2, True),
    ('1', 0, 2, True),
    ('2', 0, 2, True),
    ('3', 0, 2, False),
])
def test_check_bounds(val, low, high, expected):
    assert puzzle04b.check_bounds(val, low, high) == expected


@pytest.mark.parametrize('hgt, expected', [
    ('1', False),
    ('60', False),
    ('58in', False),
    ('59in', True),
    ('150', False),
    ('150cm', True),
    ('150cm ', False),
    ('193cm', True),
    ('194cm', False),
])
def test_check_height(hgt, expected):
    assert puzzle04b.check_height(hgt) == expected

