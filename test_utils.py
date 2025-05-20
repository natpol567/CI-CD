import pytest
from src.utils import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3), (0,0,0), (-1,1,0),
])
def test_add(a,b,expected):
    assert add(a,b) == expected

# analogicznie testy dla subtract, multiply

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1,0)
