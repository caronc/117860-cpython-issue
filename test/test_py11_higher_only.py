import sys
from unittest import mock


# This actually retrives apprise.Apprise.Apprise().notify when using
# earlier versions of py.test (hence apprise.__init__.__all__ is respected)
@mock.patch("apprise.Apprise.Apprise.notify")
def test_py10_and_lower_fails(mock_notify):
    """
    Only works with Python >= v3.11

    Python v3.10 and lower produces:
    ModuleNotFoundError: No module named 'apprise.Apprise.Apprise'; 'apprise.Apprise' is not a package
    """
    pass
