"""
Utils for testing
"""
from django.db.models import fields

def get_simplified_model(**kwargs):
    """
    Generates a mocked model class

    Expected kwargs:
    - `fields`: dict field_name:field_instance that will populate the model fields

    :returns: InternalSimplifiedModel
    """
    model_fields = {
        "id": fields.AutoField(name="id"),
    }
    name = "SimplifiedModel"

    if "fields" in kwargs:
        model_fields.update(kwargs.get("fields"))

    class InternalSimplifiedModel(object):
        """
        Fake model class, as django will require
        a DJANGO_SETTINGS_MODULE module.

        The class offers the mocked functionality
        expected to be used by the library
        """

        class _meta(object):
            """Fake meta class"""
            pk = 0
            model_name = "SIMPLIFIED_MODEL_NAME"

            @classmethod
            def get_fields(cls):
                """Fake get_fields"""
                return model_fields.values()

        class objects(object): # pylint: disable=C0103
            """Fake object manager"""

            @classmethod
            def create(cls, *args, **kwargs):
                """Fake create"""
                return {
                    "args": args,
                    "kwargs": kwargs,
                }

    InternalSimplifiedModel.__name__ = name

    return InternalSimplifiedModel

class SimplifiedForeignKey(fields.related.ForeignKey):
    """
    Simplified foreign key class
    """

    def __init__(self, **kwargs):
        """
        Sets the defaults for the class
        """
        kwargs["on_delete"] = ""
        super().__init__(get_simplified_model(), **kwargs)

SimplifiedForeignKey.__name__ = "ForeignKey"

TESTED_FIELDS = (
    fields.IntegerField,
    fields.FloatField,
    fields.CharField,
    fields.TextField,
    fields.EmailField,
    fields.BooleanField,
    fields.DateField,
    fields.DateTimeField,
    SimplifiedForeignKey,
)
