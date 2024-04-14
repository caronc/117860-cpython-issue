# Python v3.10 and >3.11 Handle Imports Incorrectly
This repository was created to show that the `__all__` references within a module being mocked are not honored in versions of Python v3.11 and higher.

This repository was created to cross reference Issue: [cpython/117860](https://github.com/python/cpython/issues/117860). The failed Git Action tasks associate wit this repository demonstrate the inconsistency in the handling of `unittest.mock.patch()` importing.

All versions of Python (v2.x+, and 3.x) up until v3.10 successfully allow mocking of Apprise notify function as:
- `unittest.mock.patch('apprise.Apprise.notify')`

However this breaks in the introduction of Python v3.11 (and v3.12 also) requiring that the patch declaration change to:
- `unittest.mock.patch('apprise.Apprise.Apprise.notify')`

The problem is the new required path is not backwards compatible with previous versions of Python, and the old required path is not compatible with the new.

The original path is the correct one; something changed in Python v3.11 that caused the import rules to be ignored.  _This however is NOT the case for just a regular import of the module (outside of `unittest`)_.  Python v3.11 still allows a `from apprise import Apprise` which is correct (and further pointing out the new inconsitency).

## Demonstration
First acquire this repository into your own environment:
```bash
# Clone repo
git clone git@github.com:caronc/117860-cpython-issue.git

# Change into our directory
cd 117860-cpython-issue
```

Now in this directory there are 3 Dockerfiles you can use.
1. Python v3.10; this one works perfect (based on `python:3.10-buster`):
   ```bash
   docker-compose run --service-ports --rm test.py310 pytest
   ```

   It will fail to run the tests I had to modify to make worth with Python v3.11+ as the do not honor the `__all__` and Python v3.10 does. It throws:
   ```
   # test/test_py11_higher_only.py
   ModuleNotFoundError: No module named 'apprise.Apprise.Apprise'; 'apprise.Apprise' is not a package
   ```
1. Python v3.11; this one however fails (based on `python:3.11-buster`):
   ```bash
   docker-compose run --service-ports --rm test.py311 pytest
   ```
   It will throw:
   ```
   # test/test_py10_lower_only.py
   AttributeError: <module 'apprise.Apprise' from '/usr/local/lib/python3.11/site-packages/apprise/Apprise.py'> does not have the attribute 'notify'
   ```

   This demonstrates that the `__all__` is not being properly referenced. What is interesting is that importing the module directly works fine in this version (proving that the `__all__` is however being honorted _in some cases_ ).  You can witness this by doing the following:
   ```bash
   docker-compose run --service-ports --rm test.py311 python
   ```
   Then type:
   ```python
   # Thanks to __all__ functionality; this is actually apprise.Apprise.Apprise
   # but made easy
   from apprise import Apprise

   # You will safetly land here and can now do something like:
   ap_obj = Apprise()
   ```

You can see the `__all__` reference in the Apprise source [here](https://github.com/caronc/apprise/blob/cced5ed7b559a8d1f0cddd6e940e60571949ad8a/apprise/__init__.py) which is located in the `apprise.__init__.py` file to make the class imports easier for external users.

## Expected Results
- The `test/test_py11_higher_only.py` is a bad test all around and should fail with all Python versions
- The `test/test_py10_lower_only.py` _should_ work with all Python versions

