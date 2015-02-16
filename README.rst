.. image:: https://travis-ci.org/crdoconnor/xeger.svg?branch=master
    :target: https://travis-ci.org/crdoconnor/xeger

Xeger
=====

Library to generate random strings from regular expressions.

To install, type:

::

    pip install xeger


To use, type:

>>> import xeger
>>> xeger.xeger("/json/([0-9]+)", limit=10)  # default limit = 10
u'/json/15062213'


About
=====

Code borrowed and cleaned up from `the python module
rstr by Leap Frog Development <http://jpmens.net/2010/04/26/resty/>`,
in turn inspired by the Java library `Xeger <http://code.google.com/p/xeger/>`.
