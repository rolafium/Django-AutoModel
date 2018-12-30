"""
Get values functions for all the fields
"""
from django_auto_model.utils import get_now, get_prefixed_str


def _get_value_for_integer_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for IntegerField

    :param field: django.db.models.field.IntegerField
    :returns: int
    """
    return 0

def _get_value_for_float_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for FloatField

    :param field: django.db.models.field.FloatField
    :returns: float
    """
    return 0

def _get_value_for_char_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for CharField

    :param field: django.db.models.field.CharField
    :returns: str
    """
    return get_prefixed_str(field.name)

def _get_value_for_text_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for TextField

    :param field: django.db.models.field.TextField
    :returns: str
    """
    return get_prefixed_str(field.name)

def _get_value_for_email_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for EmailField

    :param field: django.db.models.field.EmailField
    :returns: str
    """
    return get_prefixed_str("email@email.email")

def _get_value_for_boolean_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for BooleanField

    :param field: django.db.models.field.BooleanField
    :returns: bool
    """
    return False

def _get_value_for_date_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for DateField

    :param field: django.db.models.field.DateField
    :returns: datetime.date
    """
    return get_now().date()

def _get_value_for_date_time_field(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for DateTimeField

    :param field: django.db.models.field.DateTimeField
    :returns: datetime.datetime
    """
    return get_now()

def _get_value_for_foreign_key(model_creator, field): # pylint: disable=W0613
    """
    Generates the default value for ForeignKey

    :param field: django.db.models.field.ForeignKey
    :returns: django.db.models.Model child class instance
    """
    if field.null:
        return None
    return model_creator.create_model(field.remote_field.model)
