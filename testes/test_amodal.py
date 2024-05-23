import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, resultado", [
    ([1, 2, 3, 4, 5], "Não existe moda"),
    ([1, 2, 2, 3, 4], "Existe moda")
])
def test_amodal(lista, resultado):
    assert StatsN2.amodal(lista) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.amodal([1, 2, 3, 4, 5]) == "Existe moda"
