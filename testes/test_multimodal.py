import pytest
from StatsN2 import StatsN2

@pytest.mark.parametrize("lista, resultado", [
    ([1, 2, 2, 3, 3], [2, 3]),
    ([2, 2, 3, 3, 4, 4], [2, 3, 4])
])
def test_multimodal(lista, resultado):
    assert StatsN2.multimodal(lista) == resultado

@pytest.mark.xfail(reason="This test is expected to fail")
def test_fail():
    assert StatsN2.multimodal([1, 2, 3, 4, 5]) == [2]
