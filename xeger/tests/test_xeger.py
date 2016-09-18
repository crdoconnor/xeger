import re
import unittest
import xeger

class TestXeger(unittest.TestCase):
    def setUp(self):
        pass

    def match(self, pattern):
        for _ in range(100):
            assert re.match(pattern, xeger.xeger(pattern))

    def test_single_dot(self):
        """
        Verify that the dot character produces only a single character.
        """
        self.match(r'^.$')

    def test_dot(self):
        """
        Verify that the dot character doesn't produce newlines.
        See: https://bitbucket.org/leapfrogdevelopment/rstr/issue/1/
        """
        for i in range(100):
            self.match(r'.+')

    def test_date(self):
        self.match(r'^([1-9]|0[1-9]|[12][0-9]|3[01])\D([1-9]|0[1-9]|1[012])\D(19[0-9][0-9]|20[0-9][0-9])$')

    def test_up_to_closing_tag(self):
        self.match(r'([^<]*)')

    def test_ipv4(self):
        self.match(r'^(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]){3}$')

    def test_year_1900_2099(self):
        self.match(r'^(19|20)[\d]{2,2}$')

    def test_positive_or_negative_number(self):
        self.match(r'^-{0,1}\d*\.{0,1}\d+$')

    def test_positive_integers(self):
        self.match(r'^\d+$')

    def test_email_complicated(self):
        self.match(r'^([0-9a-zA-Z]([\+\-_\.][0-9a-zA-Z]+)*)+"@(([0-9a-zA-Z][-\w]*[0-9a-zA-Z]*\.)+[a-zA-Z0-9]{2,17})$')

    def test_email(self):
        self.match(r'(.*?)\@(.*?)\.(.*?)')

    def test_alpha(self):
        self.match(r'[:alpha:]')

    def test_zero_or_more_anything_non_greedy(self):
        self.match(r'(.*?)')

    def test_zero_or_more_greedy(self):
        self.match(r'(.*)')

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
