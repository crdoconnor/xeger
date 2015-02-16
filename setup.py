import os, sys, re, codecs
from setuptools import setup, find_packages

def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

long_description = read('README.rst')

setup(name="xeger",
      version="0.1",
      description="A library for generating random strings from a valid regular expression.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
      ],
      keywords='regular expressions regexpx random generator',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      license='BSD',
      package_data={},
      zip_safe=False,
      test_suite='xeger.tests.suite',
)
