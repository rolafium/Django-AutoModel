"""
Tests for snakelize
module: django_auto_model.utils
"""
import datetime
from django_auto_model.utils import get_now

def test_is_datetime():
    """Should be a datetime instance"""
    now = get_now()
    assert isinstance(now, datetime.datetime)

def test_value_is_close_to_now():
    """Should be close enough to the test execution time"""
    before = datetime.datetime.now()
    now = get_now()
    after = datetime.datetime.now()

    assert now >= before
    assert now <= after

def test_objects_are_not_singleton():
    """Different calls to the function return different instances"""
    now1 = get_now()
    now2 = get_now()

    assert now1 is not now2
