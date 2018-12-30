"""
Utils module
Defines utility functions used
internally by the library
"""
import re
import datetime
import random

def get_prefixed_str(original_str):
    """
    Returns a new string that is prefixed
    with a random number (range 0-10000)

    This function is used to go around the uniqueness
    of certain fields when creating more instances of the model,
    most notably the django.contrib.auth.models.User.username field
    will throw IntegrityError if two users will share the same username

    :returns: str
    """
    return "{prefix}__{original_str}".format(
        prefix=random.randint(0, 10000),
        original_str=original_str,
    )

def get_now():
    """
    Returns a UTC timezoned datetime.datetime.now()
    as django expects all datetime values to be tz aware

    :returns: datetime.datetime
    """
    now = datetime.datetime.now()
    now.replace(tzinfo=datetime.timezone.utc)
    return now

def snakelize(camel_cased_str):
    """
    Convers a PascalCase str to snake_case

    :returns: str
    """
    return "_".join(
        word.lower()
        for word in re.findall('[A-Z][^A-Z]*', camel_cased_str)
    )
