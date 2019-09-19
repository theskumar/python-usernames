python-usernames
================

|Build Status| |Coverage Status| |PyPI version|

Python library to validate usernames suitable for use in public facing
applications where use can choose login names and sub-domains.

Features
--------

-  Provides a default regex validator
-  Validates against list of `banned
   words <https://github.com/theskumar/python-usernames/blob/master/usernames/reserved_words.py>`__
   that should not be used as username.
-  Python 2.7, 3.4, 3.5, 3.6, 3.7 pypi

Installation
------------

::

    pip install python-usernames

Usages
------

.. code:: python

    from usernames import is_safe_username

    >>> is_safe_username("jerk")
    False  # contains one of the banned words

    >>> is_safe_username("handsome!")
    False  # contains non-url friendly `!`


**is\_safe\_username** takes the following optional arguments:

-  ``whitelist``: a list of words that should be considered as always
   safe. Default: ``[]``
-  ``blacklist``: a list of words that should be considered as unsafe. Default: ``[]``
-  ``max_length``: specify the maximun character a username can have. Default: ``None``
-  ``regex``: regular expression string that must pass before the banned
   words is checked.
The default regular expression is as follows:

::

    ^                       # beginning of string
    (?!_$)                  # no only _
    (?![-.])                # no - or . at the beginning
    (?!.*[_.-]{2})          # no __ or _. or ._ or .. or -- inside
    [a-zA-Z0-9_.-]+         # allowed characters, atleast one must be present
    (?<![.-])               # no - or . at the end
    $                       # end of string

**Further Reading**

- `Let’s talk about usernames <https://www.b-list.org/weblog/2018/feb/11/usernames/>`__

**Note:**

Words like ``bigcock12`` will validated just fine, only equality against
the `banned word lists <https://github.com/theskumar/python-usernames/blob/master/usernames/reserved_words.py>`__
is checked. We don't try to be smart to avoid `Scunthorpe problem <https://en.wikipedia.org/wiki/Scunthorpe_problem>`__.
If you can come up with a algorithm/solution, please create an issue/pr :).

License
-------

MIT

.. |Build Status| image:: https://travis-ci.org/theskumar/python-usernames.svg?branch=v0.1.0
   :target: https://travis-ci.org/theskumar/python-usernames
.. |Coverage Status| image:: https://coveralls.io/repos/theskumar/python-usernames/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/theskumar/python-usernames?branch=master
.. |PyPI version| image:: https://badge.fury.io/py/python-usernames.svg
   :target: http://badge.fury.io/py/python-usernames
