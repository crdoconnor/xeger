"""Library to generate random strings from regular expressions.
Code borrowed and cleaned up from the python module rstr:
https://bitbucket.org/leapfrogdevelopment/rstr/

In turn inspired by the Java library Xeger:
http://code.google.com/p/xeger/
"""
import re
import sys
import string
import itertools
from random import choice, randint

if sys.version_info[0] >= 3:
    unichr = chr
    xrange = range


class Xeger(object):
    def __init__(self, limit=10):
        super(Xeger, self).__init__()
        self._limit = limit
        self._cache = dict()

        self._alphabets = {
            'printable': string.printable,
            'letters': string.ascii_letters,
            'uppercase': string.ascii_uppercase,
            'lowercase': string.ascii_lowercase,
            'digits': string.digits,
            'punctuation': string.punctuation,
            'nondigits': string.ascii_letters + string.punctuation,
            'nonletters': string.digits + string.punctuation,
            'whitespace': string.whitespace,
            'nonwhitespace': string.printable.strip(),
            'normal': string.ascii_letters + string.digits + ' ',
            'word': string.ascii_letters + string.digits + '_',
            'nonword': ''.join(set(string.printable)
                            .difference(string.ascii_letters +
                                        string.digits + '_')),
            'postalsafe': string.ascii_letters + string.digits + ' .-#/',
            'urlsafe': string.ascii_letters + string.digits + '-._~',
            'domainsafe': string.ascii_letters + string.digits + '-'
        }

        self._categories = {
            "category_digit": lambda: self._alphabets['digits'],
            "category_not_digit": lambda: self._alphabets['nondigits'],
            "category_space": lambda: self._alphabets['whitespace'],
            "category_not_space": lambda: self._alphabets['nonwhitespace'],
            "category_word": lambda: self._alphabets['word'],
            "category_not_word": lambda: self._alphabets['nonword'],
        }

        self._cases = {
            "literal": lambda x: unichr(x),
            "not_literal":
                lambda x: choice(string.printable.replace(unichr(x), '')),
            "at": lambda x: '',
            "in": lambda x: self._handle_in(x),
            "any": lambda x: choice(string.printable.replace('\n', '')),
            "range": lambda x: [unichr(i) for i in xrange(x[0], x[1] + 1)],
            "category": lambda x: self._categories[str(x).lower()](),
            'branch':
                lambda x: ''.join(self._handle_state(i) for i in choice(x[1])),
            "subpattern": lambda x: self._handle_group(x),
            "assert": lambda x: ''.join(self._handle_state(i) for i in x[1]),
            "assert_not": lambda x: '',
            "groupref": lambda x: self._cache[x],
            'min_repeat': lambda x: self._handle_repeat(*x),
            'max_repeat': lambda x: self._handle_repeat(*x),
            'negate': lambda x: [False],
        }

    def xeger(self, string_or_regex):
        try:
            pattern = string_or_regex.pattern
        except AttributeError:
            pattern = string_or_regex

        parsed = re.sre_parse.parse(pattern)
        result = self._build_string(parsed)
        self._cache.clear()
        return result

    def _build_string(self, parsed):
        newstr = []
        for state in parsed:
            newstr.append(self._handle_state(state))
        return ''.join(newstr)

    def _handle_state(self, state):
        opcode, value = state
        return self._cases[str(opcode).lower()](value)

    def _handle_group(self, value):
        if sys.version_info < (3,6):
            result = ''.join(self._handle_state(i) for i in value[1])
        else:
            result = ''.join(self._handle_state(i) for i in value[3])
        if value[0]:
            self._cache[value[0]] = result
        return result

    def _handle_in(self, value):
        candidates = list(itertools.chain(*(self._handle_state(i) for i in value)))
        if candidates[0] is False:
            candidates = set(string.printable).difference(candidates[1:])
            return choice(list(candidates))
        else:
            return choice(candidates)

    def _handle_repeat(self, start_range, end_range, value):
        result = []
        end_range = min((end_range, self._limit))
        times = randint(start_range, end_range)
        for i in xrange(times):
            result.append(''.join(self._handle_state(i) for i in value))
        return ''.join(result)
