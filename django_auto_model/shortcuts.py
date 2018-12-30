"""
Shortcuts module.
Defines shortcuts for the library
"""
from django_auto_model.creator import ModelCreator


def create_model(model):
    """
    Creates a model instance.

    Wrapper over ModelCreator.create_model -
    See ModelCreator.create_model documentation

    :param model: django.db.models.Model child class
    :returns: django.db.models.Model child class instance
    """
    return ModelCreator.create_model(model)
