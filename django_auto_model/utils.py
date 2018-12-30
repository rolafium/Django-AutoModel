import re
import datetime
import random

def get_none(field):
    return None

def get_prefixed_str(original_str):
    return "{prefix}__{original_str}".format(
        prefix=random.randint(0, 10000),
        original_str=original_str,
    )

def get_now():
    dt = datetime.datetime.now()
    dt.replace(tzinfo=datetime.timezone.utc)
    return dt

def snakelize(s):
    return "_".join(
        word.lower()
        for word in re.findall('[A-Z][^A-Z]*', s)
    )
