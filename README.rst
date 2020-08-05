.. image:: https://travis-ci.org/crdoconnor/xeger.svg?branch=master
    :target: https://travis-ci.org/crdoconnor/xeger

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

Code adapted and refactored from the Python library
`rstr by Leapfrog Online <https://github.com/leapfrogonline/rstr>`_ (now iProspect),
in turn inspired by the Java library `Xeger <http://code.google.com/p/xeger/>`_.
