import sys

import pytest
from app import message_service



def test_compat_urlsafe_b64encode():
    with pytest.raises(AttributeError):
        message_service.compat_urlsafe_b64encode(1)


def test_send_message():
    pass


def test_create_message():
    with pytest.raises(AttributeError):
        message_service.create_message('Test', 'Test', 'Test', 22)


def test_create_message_answerType():
    answer = message_service.create_message('Test', 1, 'Test', 'Test')
    assert isinstance(answer, dict)
