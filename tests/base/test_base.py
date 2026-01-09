import pytest

def test_pytest_raises_valid_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
