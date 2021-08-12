import itertools
import re
import unittest
import xeger
import pytest


def match(pattern):
    for _ in range(100):
        assert re.match(pattern, xeger.xeger(pattern))


def test_single_dot():
    """
    Verify that the dot character produces only a single character.
    """
    match(r'^.$')


def test_dot():
    """
    Verify that the dot character doesn't produce newlines.
    See: https://bitbucket.org/leapfrogdevelopment/rstr/issue/1/
    """
    for i in range(100):
        match(r'.+')


def test_date():
    match(r'^([1-9]|0[1-9]|[12][0-9]|3[01])\D([1-9]|0[1-9]|1[012])\D(19[0-9][0-9]|20[0-9][0-9])$')


def test_up_to_closing_tag():
    match(r'([^<]*)')


def test_ipv4():
    match(r'^(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]){3}$')


def test_year_1900_2099():
    match(r'^(19|20)[\d]{2,2}$')


def test_positive_or_negative_number():
    match(r'^-{0,1}\d*\.{0,1}\d+$')


def test_positive_integers():
    match(r'^\d+$')


def test_email_complicated():
    match(r'^([0-9a-zA-Z]([\+\-_\.][0-9a-zA-Z]+)*)+"@(([0-9a-zA-Z][-\w]*[0-9a-zA-Z]*\.)+[a-zA-Z0-9]{2,17})$')


def test_email():
    match(r'(.*?)\@(.*?)\.(.*?)')


def test_alpha():
    match(r'[:alpha:]')


def test_zero_or_more_anything_non_greedy():
    match(r'(.*?)')


def test_literals():
    match(r'foo')


def test_digit():
    match(r'\d')


def test_nondigits():
    match(r'\D')


def test_literal_with_repeat():
    match(r'A{3}')


def test_literal_with_range_repeat():
    match(r'A{2, 5}')


def test_word():
    match(r'\w')


def test_nonword():
    match(r'\W')


def test_or():
    match(r'foo|bar')


def test_or_with_subpattern():
    match(r'(foo|bar)')


def test_range():
    match(r'[A-F]')


def test_character_group():
    match(r'[ABC]')


def test_caret():
    match(r'^foo')


def test_dollarsign():
    match(r'foo$')


def test_not_literal():
    match(r'[^a]')


def test_negation_group():
    match(r'[^AEIOU]')


def test_lookahead():
    match(r'foo(?=bar)')


def test_lookbehind():
    pattern = r'(?<=foo)bar'
    assert re.search(pattern, xeger.xeger(pattern))


def test_backreference():
    match(r'(foo|bar)baz\1')


def test_zero_or_more_greedy():
    match(r'a*')
    match(r'(.*)')


def test_zero_or_more_non_greedy():
    match(r'a*?')


@pytest.mark.parametrize("limit", range(5))
def test_incoherent_limit_and_qualifier(limit):
    r = xeger.Xeger(limit=limit)
    o = r.xeger(r'a{2}')
    assert len(o) == 2


@pytest.mark.parametrize("seed", [777, 1234, 369, 8031])
def test_xeger_object_seeding(seed):
    xg1 = xeger.Xeger(seed=seed)
    string1 = xg1.xeger(r'\w{3,4}')

    xg2 = xeger.Xeger(seed=seed)
    string2 = xg2.xeger(r'\w{3,4}')

    assert string1 == string2


def test_xeger_random_instance():
    xg1 = xeger.Xeger()
    xg_random = xg1.random

    xg2 = xeger.Xeger()
    xg2.random = xg_random

    assert xg1.random == xg2.random
    # xg_random is used by both, so if we give 
    # the same seed, the result should be the same

    xg_random.seed(90)
    string1 = xg1.xeger(r'\w\d\w')
    xg_random.seed(90)
    string2 = xg2.xeger(r'\w\d\w')

    assert string1 == string2


def test_xeger():
    assert xeger.Xeger(seed=0).xeger('.{1,8}') == xeger.Xeger(seed=0).xeger('.{1,8}')


if __name__ == '__main__':
    pytest.main([__file__, '-vv'])
