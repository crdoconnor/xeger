.. image:: https://travis-ci.org/pousisk/xeger.svg?branch=master
    :target: https://travis-ci.org/poussik/xeger

Xeger
=====

Library to generate random strings from regular expressions.

To install, type:

::

    pip install xeger


To use, type:

>>> from xeger import Xeger
>>> x = Xeger(limit=10)  # default limit = 10
>>> x.xeger("/json/([0-9]+)")
u'/json/15062213'


About
=====

Code borrowed and cleaned up from `the python module
rstr by Leap Frog Development <http://jpmens.net/2010/04/26/resty/>`,
in turn inspired by the Java library `Xeger <http://code.google.com/p/xeger/>`.
