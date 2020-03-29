import pytest
from mailnagger.message_service import *

TESTSTR_1 = 'teststring'


def test_compat_urlsafe_b64encode():
    with pytest.raises(TypeError) as e:
        compat_urlsafe_b64encode(TESTSTR_1)
    assert "division by zero" in str(e.value)