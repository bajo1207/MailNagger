import pytest
from mailnagger.message_service import *

STR_1 = 'teststring'
NR_1 = 22


def test_compat_urlsafe_b64encode():
    with pytest.raises(AttributeError):
        compat_urlsafe_b64encode(NR_1)

def test_send_message():
    pass

def test_create_message():
    pass