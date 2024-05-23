import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, pesos, resultado", [
    ([1, 2, 3, 4, 5], [0.1, 0.2, 0.3, 0.2, 0.2], 3.2),
    ([2, 4, 6, 8, 10], [0.1, 0.2, 0.3, 0.2, 0.2], 6.2)
])
def test_media_ponderada(lista, pesos, resultado):
    assert StatsN2.media_ponderada(lista, pesos) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.media_ponderada([1, 2, 3, 4, 5], [0.1, 0.2, 0.3, 0.2, 0.2]) == 2.5
