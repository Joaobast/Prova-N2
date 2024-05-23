import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, resultado", [
    ([1, 2, 3, 4, 5], 2.5),
    ([2, 4, 6, 8, 10], 10.0)
])
def test_variancia(lista, resultado):
    assert StatsN2.variancia(lista) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.variancia([1, 2, 3, 4, 5]) == 1.5
