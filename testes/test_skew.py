import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, resultado", [
    ([1, 2, 3, 4, 5], "Distribuição normal"),
    ([2, 2, 3, 3, 4, 4], "Distribuição normal")
])
def test_skew(lista, resultado):
    assert StatsN2.skew(lista) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.skew([1, 2, 3, 4, 5]) == "Distribuição assimétrica"
