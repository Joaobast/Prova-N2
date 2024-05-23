import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, resultado", [
    ([1, 2, 2, 3, 4], 2),
    ([2, 2, 3, 3, 4], 2)
])
def test_unimodal(lista, resultado):
    assert StatsN2.unimodal(lista) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.unimodal([1, 2, 3, 4, 5]) == 2
