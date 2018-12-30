"""
Tests for snakelize
module: django_auto_model.utils
"""
import pytest
from django_auto_model.utils import snakelize

@pytest.mark.parametrize("input_str,output_str", (
    ("A", "a"),
    ("Aa", "aa"),
    ("AA", "a_a"),
    ("AaA", "aa_a"),
    ("AAa", "a_aa"),
    ("AaAa", "aa_aa"),
    ("IntegerField", "integer_field"),
    ("FloatField", "float_field"),
    ("BooleanField", "boolean_field"),
    ("CharField", "char_field"),
    ("DateField", "date_field"),
    ("TextField", "text_field"),
    ("DateTimeField", "date_time_field"),
    ("ForeignKey", "foreign_key"),
))
def test_snakelize_values(input_str, output_str):
    """Should return the snake_case version of the input string"""
    assert snakelize(input_str) == output_str
