import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, resultado", [
    ([1, 2, 3, 4, 5], 3.0),
    ([2, 4, 6, 8, 10], 6.0)
])
def test_mediana(lista, resultado):
    assert StatsN2.mediana(lista) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.mediana([1, 2, 3, 4, 5]) == 2.5
