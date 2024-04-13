# Python v3.10 and >3.11 Testing Reflection of `__all__`
This repository was created to show that the `__all__` references within a module being mocked are not honored in versions of Python v3.11 and higher.

# Demonstration
First acquire this repository into your own environment:
```bash
# Clone repo
git clone git@github.com:caronc/mytest.git

# Change into our directory
cd mytest
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
- The `test/test_py10_lower_only.py` should work with all Python versions

