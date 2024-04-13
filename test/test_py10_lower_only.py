import sys
from unittest import mock


# This actually retrives apprise.Apprise.Apprise().notify when using
# earlier versions of py.test (hence apprise.__init__.__all__ is respected)
@mock.patch("apprise.Apprise.notify")
def test_py11_and_higher_fails(mock_notify):
    """
    Only works with Python v3.10

    Python v3.11+ produces (where ?? is swapped with 11, or 12 respectively to whichever version of Pythong is being tested):
    AttributeError: <module 'apprise.Apprise' from '/usr/local/lib/python3.??/site-packages/apprise/Apprise.py'> does not have the attribute 'notify
    """
    pass
