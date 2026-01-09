import pytest

def test_rejects_string_input():
    with pytest.raises(TypeError, match="str"):
        pytest.raises("invalid")

def test_rejects_none_input():
    with pytest.raises(TypeError, match="NoneType"):
        pytest.raises(None)
