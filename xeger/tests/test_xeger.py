import re
import unittest
import xeger

class TestXeger(unittest.TestCase):
    def setUp(self):
        pass

    def match(self, pattern):
        assert re.match(pattern, xeger.xeger(pattern))

    def test_dot(self):
        """
        Verify that the dot character doesn't produce newlines.
        See: https://bitbucket.org/leapfrogdevelopment/rstr/issue/1/
        """
        for i in range(100):
            self.match(r'.+')

    def test_literals(self):
        self.match(r'foo')

    def test_digit(self):
        self.match(r'\d')

    def test_nondigits(self):
        self.match(r'\D')

    def test_literal_with_repeat(self):
        self.match(r'A{3}')

    def test_literal_with_range_repeat(self):
        self.match(r'A{2, 5}')

    def test_word(self):
        self.match(r'\w')

    def test_nonword(self):
        self.match(r'\W')

    def test_or(self):
        self.match(r'foo|bar')

    def test_or_with_subpattern(self):
        self.match(r'(foo|bar)')

    def test_range(self):
        self.match(r'[A-F]')

    def test_character_group(self):
        self.match(r'[ABC]')

    def test_caret(self):
        self.match(r'^foo')

    def test_dollarsign(self):
        self.match(r'foo$')

    def test_not_literal(self):
        self.match(r'[^a]')

    def test_negation_group(self):
        self.match(r'[^AEIOU]')

    def test_lookahead(self):
        self.match(r'foo(?=bar)')

    def test_lookbehind(self):
        pattern = r'(?<=foo)bar'
        assert re.search(pattern, xeger.xeger(pattern))

    def test_backreference(self):
        self.match(r'(foo|bar)baz\1')

    def test_zero_or_more_greedy(self):
        self.match(r'a*')

    def test_zero_or_more_non_greedy(self):
        self.match(r'a*?')
