"""
Tests for get_prefixed_str
module: django_auto_model.utils
"""
import pytest
from django_auto_model.utils import get_prefixed_str


def test_output_is_string():
    """Should be instance of str"""
    prefixed = get_prefixed_str("original_string")
    assert isinstance(prefixed, str)

@pytest.mark.parametrize("original_str", (
    "",
    "A",
    "a",
    "_abc",
    "__abc",
    "123__abc",
    "_123__abc",
    "__123__abc",
    "a__123__abc",
    "_a__123__abc",
    "__a__123__abc",
    "_______a",
    "_______a__123",
    "A_",
    "A__",
    "A______",
    u"ABC",
))
def test_prefixed_values(original_str):
    """Should return the snake_case version of the input string"""
    prefixed = get_prefixed_str(original_str)
    splits = prefixed.split("__")
    prefix = int(splits[0])

    assert original_str in prefixed
    assert original_str in "__".join(splits[1:])
    assert prefix >= 0
    assert prefix <= 10000
