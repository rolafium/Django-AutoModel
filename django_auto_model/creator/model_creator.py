"""
Model creator module

This module contains classes and functions
that help library consumers to automatically
generate models in their tests.
"""
from django_auto_model.utils import snakelize
from django_auto_model.creator import fields

class ModelCreator(object):
    """
    Class handler that allows consumers
    to create model instances without
    specifying any field parameter.

    All methods are classmethods to allow users
    to inherit the class and customise its behaviour
    (i.e. returning different default values)
    """

    # List of fields that we don't need
    # to pass to the model.objects.create method
    # as they are automatically handled by django
    SKIP_LIST = [
        "AutoField",
        "ManyToOneRel",
        "ManyToManyField",
    ]

    @classmethod
    def create_model(cls, model):
        """
        Creates an instance of the specified model.
        Tries to populate all the values with the
        field defaults specified on the model.

        If it fails, generates a meaningful
        default for the field.

        If it encounters a field included
        in cls.SKIP_LIST, it ignores it.

        If it encounters a ForeignKey,
        calls cls.create_model on the related model,
        de facto generating the whole dependency tree.

        :param model: django.db.models.Model child class
        :returns: django.db.models.Model child class instance
        """
        creation_values = {
            field.name: cls._get_value_for_field(field)
            for field in model._meta.get_fields() # pylint: disable=W0212
            if field.__class__.__name__ not in cls.SKIP_LIST
        }
        return model.objects.create(**creation_values)

    @classmethod
    def _get_field_func(cls, field):
        """
        Internal function that maps a field to its value function.

        :param field: django.db.models.field instance
        :returns: function
        """
        func_name = "_get_value_for_" + snakelize(field.__class__.__name__)
        return getattr(cls, func_name)

    @classmethod
    def _get_value_for_field(cls, field):
        """
        Internal function that generates a value for the specified field.

        :param field: django.db.models.field instance
        :returns: any
        """
        if field.has_default():
            return field.get_default()

        field_func = cls._get_field_func(field)
        field_value = field_func(field)

        return field_value


# pylint: disable=W0212
ModelCreator._get_value_for_integer_field = classmethod(fields._get_value_for_integer_field)
ModelCreator._get_value_for_float_field = classmethod(fields._get_value_for_float_field)
ModelCreator._get_value_for_char_field = classmethod(fields._get_value_for_char_field)
ModelCreator._get_value_for_text_field = classmethod(fields._get_value_for_text_field)
ModelCreator._get_value_for_email_field = classmethod(fields._get_value_for_email_field)
ModelCreator._get_value_for_boolean_field = classmethod(fields._get_value_for_boolean_field)
ModelCreator._get_value_for_date_field = classmethod(fields._get_value_for_date_field)
ModelCreator._get_value_for_date_time_field = classmethod(fields._get_value_for_date_time_field)
ModelCreator._get_value_for_foreign_key = classmethod(fields._get_value_for_foreign_key)
