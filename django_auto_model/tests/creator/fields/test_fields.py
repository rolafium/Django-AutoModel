"""
Tests for the fields get_value functions
module: django_auto_model.creator.fields
"""
import datetime
import pytest
from django.db.models import fields as django_fields
from django_auto_model.tests.resources import get_simplified_model
from django_auto_model.utils import get_now
from django_auto_model.creator import ModelCreator, fields


# pylint: disable=W0212

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.IntegerField(), 0),
    (django_fields.IntegerField(name="A"), 0),
))
def test_get_value_for_integer_field(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_integer_field(ModelCreator, field)
    assert actual_value == expected_value

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.FloatField(), 0),
    (django_fields.FloatField(name="A"), 0),
))
def test_get_value_for_float_field(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_float_field(ModelCreator, field)
    assert actual_value == expected_value

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.CharField(), "None"),
    (django_fields.CharField(name="A"), "A"),
    (django_fields.CharField(max_length=999), "None"),
    (django_fields.CharField(name="B", max_length=999), "B"),
))
def test_get_value_for_char_field(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_char_field(ModelCreator, field)
    assert isinstance(actual_value, str)
    assert expected_value in actual_value

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.TextField(), "None"),
    (django_fields.TextField(name="A"), "A"),
))
def test_get_value_for_text_field(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_text_field(ModelCreator, field)
    assert isinstance(actual_value, str)
    assert expected_value in actual_value

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.EmailField(), "email@email.email"),
    (django_fields.EmailField(name="A"), "email@email.email"),
))
def test_get_value_for_email_field(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_email_field(ModelCreator, field)
    assert isinstance(actual_value, str)
    assert expected_value in actual_value

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.BooleanField(), False),
    (django_fields.BooleanField(name="A"), False),
))
def test_get_value_for_boolean_field(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_boolean_field(ModelCreator, field)
    assert actual_value == expected_value

@pytest.mark.parametrize("field", (
    django_fields.DateField(),
    django_fields.DateField(name="A"),
))
def test_get_value_for_date_field(field):
    """Value should be valid datetime.date object"""
    before = get_now().date()
    actual_value = fields._get_value_for_date_field(ModelCreator, field)
    after = get_now().date()
    assert isinstance(actual_value, datetime.date)
    assert actual_value >= before
    assert actual_value <= after

@pytest.mark.parametrize("field", (
    django_fields.DateTimeField(),
    django_fields.DateTimeField(name="A"),
))
def test_get_value_for_date_time_field(field):
    """Value should be valid datetime.datetime object"""
    before = get_now()
    actual_value = fields._get_value_for_date_time_field(ModelCreator, field)
    after = get_now()
    assert isinstance(actual_value, datetime.datetime)
    assert actual_value >= before
    assert actual_value <= after

MOCKED_INSTANCE = { "args": (), "kwargs": {} }

@pytest.mark.parametrize("field,expected_value", (
    (django_fields.related.ForeignKey(to=get_simplified_model(), on_delete=""), MOCKED_INSTANCE),
    (django_fields.related.ForeignKey(to=get_simplified_model(), on_delete="", name="A"), MOCKED_INSTANCE),
    (django_fields.related.ForeignKey(to=get_simplified_model(), on_delete="", name="A", null=True), None),
))
def test_get_value_for_foreign_key(field, expected_value):
    """Value should match the expected value"""
    actual_value = fields._get_value_for_foreign_key(ModelCreator, field)
    assert actual_value == expected_value
