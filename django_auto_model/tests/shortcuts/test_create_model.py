"""
Tests for create_model
module: django_auto_model.shortcuts
"""
import pytest
from django_auto_model.tests.resources import TESTED_FIELDS, get_simplified_model
from django_auto_model.shortcuts import create_model


@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_create_model_with_fields(field):
    """Should return the SimplifiedModel mocked instance"""
    model = get_simplified_model(fields={ "field": field(name="field") })
    mocked_instance = create_model(model)

    assert mocked_instance["args"] == ()
    assert mocked_instance["kwargs"].keys() == { "field": "" }.keys()

@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_create_model_with_fields_defaults(field):
    """Should return the SimplifiedModel mocked instance"""
    default_value = field.__class__.__name__
    model = get_simplified_model(fields={ "field": field(name="field", default=default_value) })
    mocked_instance = create_model(model)

    assert mocked_instance["args"] == ()
    assert mocked_instance["kwargs"] == { "field": default_value }
