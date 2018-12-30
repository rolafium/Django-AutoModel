"""
Tests for create_model
module: django_auto_model.shortcuts
"""
import pytest
from django_auto_model.tests.resources import TESTED_FIELDS, get_simplified_model
from django_auto_model.shortcuts import create_model


@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_create_model(field):
    """Should return the SimplifiedModel mocked instance"""
    model = get_simplified_model(fields={ "field": field(name="field") })
    mocked_instance = create_model(model)

    assert mocked_instance is not None
