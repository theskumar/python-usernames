# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name="python-usernames",
    description="Python library to validate usernames suitable for use in public facing applications.",
    long_description=readme,
    long_description_content_type="text/markdown",
    version="0.3.1",
    author="Saurabh Kumar",
    author_email="me+github@saurabh-kumar.com",
    url="http://github.com/theskumar/python-usernames",

    packages=[
        str('usernames'),
    ],
    package_dir={'usernames': 'usernames'},
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.3',
        # 'Programming Language :: Python :: 2.4',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        # 'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        # 'Environment :: Web Environment',
        # 'Framework :: Django',
    ],
    keywords=(
        'username', 'validation', 'registration', 'python', 'safe', 'signup'
    ),
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
