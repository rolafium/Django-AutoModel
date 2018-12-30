"""
Tests for ModelCreator
module: django_auto_model.creator.model_creator
"""
import pytest
from django_auto_model.tests.resources import TESTED_FIELDS, get_simplified_model
from django_auto_model.creator.model_creator import ModelCreator


# pylint: disable=W0212

@pytest.mark.parametrize("skipped_item_name", (
    "AutoField",
    "ManyToOneRel",
    "ManyToManyField",
))
def test_skip_list(skipped_item_name):
    """Checks the expected items are in the SKIP_LIST"""
    assert skipped_item_name in ModelCreator.SKIP_LIST

@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_has_get_value_func(field):
    """Checks all the get_value functions are set for the TESTED_FIELDS"""
    value_func = ModelCreator._get_field_func(field())
    assert value_func is not None

@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_get_value_for_field_with_default(field):
    """Checks the default is returned for each of the values"""
    expected_default_value = "FIELD_DEFAULT_VALUE"
    tested_field = field(default=expected_default_value)
    field_value = ModelCreator._get_value_for_field(tested_field)

    assert field_value == expected_default_value

@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_get_value_for_field_without_default(field):
    """Checks a value is produced for the field"""
    tested_field = field()
    field_value = ModelCreator._get_value_for_field(tested_field)

    assert field_value is not None

@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_create_model_with_fields(field):
    """Should return the SimplifiedModel mocked instance"""
    model = get_simplified_model(fields={ "field": field(name="field") })
    mocked_instance = ModelCreator.create_model(model)

    assert mocked_instance["args"] == ()
    assert mocked_instance["kwargs"].keys() == { "field": "" }.keys()

@pytest.mark.parametrize("field", TESTED_FIELDS)
def test_create_model_with_fields_defaults(field):
    """Should return the SimplifiedModel mocked instance"""
    default_value = field.__class__.__name__
    model = get_simplified_model(fields={ "field": field(name="field", default=default_value) })
    mocked_instance = ModelCreator.create_model(model)

    assert mocked_instance["args"] == ()
    assert mocked_instance["kwargs"] == { "field": default_value }
