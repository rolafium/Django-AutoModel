from django_auto_model.utils import get_none, get_now, get_prefixed_str, snakelize


class ModelCreator(object):

    SKIP_LIST = [
        "AutoField",
        "ManyToOneRel",
        "ManyToManyField",
    ]

    @classmethod
    def get_field_func(cls, field):
        func_name = "get_value_for_" + snakelize(field.__class__.__name__)
        return getattr(cls, func_name)


    @classmethod
    def get_value_for_integer_field(cls, field):
        return 0

    @classmethod
    def get_value_for_float_field(cls, field):
        return 0

    @classmethod
    def get_value_for_char_field(cls, field):
        return get_prefixed_str(field.name)

    @classmethod
    def get_value_for_text_field(cls, field):
        return get_prefixed_str(field.name)

    @classmethod
    def get_value_for_email_field(cls, field):
        return get_prefixed_str("email@email.email")

    @classmethod
    def get_value_for_boolean_field(cls, field):
        return False

    @classmethod
    def get_value_for_foreign_key(cls, field):
        if field.null:
            return None
        else:
            return cls.create_model(field.remote_field.model)

    @classmethod
    def get_value_for_date_field(cls, field):
        return get_now().date()

    @classmethod
    def get_value_for_date_time_field(cls, field):
        return get_now()

    @classmethod
    def get_value_for_field(cls, field):
        if field.has_default():
            return field.get_default()

        field_name = field.__class__.__name__
        field_func = cls.get_field_func(field)
        field_value = field_func(field)

        return field_value

    @classmethod
    def create_model(cls, model):
        creation_values = {
            field.name: cls.get_value_for_field(field)
            for field in model._meta.get_fields()
            if field.__class__.__name__ not in cls.SKIP_LIST
        }
        return model.objects.create(**creation_values)


def create_model(model):
    return ModelCreator.create_model(model)
