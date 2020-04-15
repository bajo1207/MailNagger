import pytest
import mailnagger.message_service

STR_1 = 'teststring'
NR_1 = 22

def test_compat_urlsafe_b64encode():
    with pytest.raises(AttributeError):
        mailnagger.message_service.compat_urlsafe_b64encode(NR_1)

def test_send_message():
    pass


def test_create_message():
    with pytest.raises(AttributeError):
        mailnagger.message_service.create_message('Test', 'Test', 'Test', 22)

def test_create_message_answerType():
    answer = mailnagger.message_service.create_message('Test', 'Test', 'Test', 'Test')
    assert isinstance(answer, dict)
