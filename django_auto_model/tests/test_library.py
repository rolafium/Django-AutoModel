"""
Tests for the library as a whole
"""
import pytest
import django_auto_model


@pytest.mark.parametrize("expected_object_name", (
    "ModelCreator",
    "create_model",
))
def test_model_creator_defined(expected_object_name):
    """Should expose the expected objects"""
    assert hasattr(django_auto_model, expected_object_name)
