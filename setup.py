"""
Based on https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

INSTALL_REQUIRES = [
    'numpy',
    'scipy',
    ]
TEST_REQUIRES = [
        'pytest',
        'coverage',
        'pytest-cov',
        'matplotlib',
    ]
DOCS_REQUIRES = [
    'sphinx_rtd_theme',
    ]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='noise_robust_differentiator',

    version='0.0.2',

    description="Python implementation of Pavel Holoborodko's smooth noise-robust differentiators",

    author='Matt Vernacchia',
    author_email='mvernacc@mit.edu',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    # What does your project relate to?
    keywords='derivative noise numerical',

    long_description=long_description,
    long_description_content_type="text/markdown",

    project_urls={
        'Source Code': 'https://github.com/mvernacc/noise_robust_differentiator',
    },

    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
        'docs': DOCS_REQUIRES + INSTALL_REQUIRES,
    },

    packages=find_packages(),

    scripts=[],
)
