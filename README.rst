Library to generate random strings from regular expressions.

Code borrowed and cleaned up from the python module rstr:
https://bitbucket.org/leapfrogdevelopment/rstr/

In turn inspired by the Java library Xeger:
http://code.google.com/p/xeger/

Use:

>>> import xeger
>>> xeger.xeger("/json/([0-9]+)", limit=10)  # default limit = 10
u'/json/15062213'

