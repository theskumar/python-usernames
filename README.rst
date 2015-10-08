python-usernames
================

|Build Status| |Coverage Status| |PyPI version| |PyPI|

Python library to validate usernames suitable for use in public facing
applications where use can choose login names and sub-domains.

Features
--------

-  Provides a default regex validator
-  Validates against list of `banned
   words <https://github.com/theskumar/python-usernames/blob/master/usernames/reserved_words.py>`__
   that should not be used as username.
-  Python 2.6, 2.7, 3.3, 3.4

Installation
------------

::

    pip install python-usernames

Usages
------

.. code:: python

    from usernames import is_safe_username

    >> is_safe_username("jerk")
    False  # contains one of the banned words
    >> is_safe_username("handsome!")
    False  # contains non-url friendly `!`

**is\_safe\_username** takes the following optional arguments:

-  ``regex``: regular expression string that must pass before the banned
   words is checked. Default is ``^[a-zA-Z0-9_.-]+$``
-  ``whitelist``: a list of words that should be considered as always
   safe.
-  ``blacklist``: a list of words that should be considered as unsafe.

License
-------

MIT

.. |Build Status| image:: https://travis-ci.org/theskumar/python-usernames.svg?branch=v0.1.0
   :target: https://travis-ci.org/theskumar/python-usernames
.. |Coverage Status| image:: https://coveralls.io/repos/theskumar/python-usernames/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/theskumar/python-usernames?branch=master
.. |PyPI version| image:: https://badge.fury.io/py/python-usernames.svg
   :target: http://badge.fury.io/py/python-usernames
.. |PyPI| image:: https://img.shields.io/pypi/dm/python-usernames.svg
   :target: https://pypi.python.org/pypi/python-usernames
