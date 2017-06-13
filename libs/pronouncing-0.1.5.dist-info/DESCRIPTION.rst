pronouncing
===========

.. image:: https://img.shields.io/travis/aparrish/pronouncingpy.svg
        :target: https://travis-ci.org/aparrish/pronouncingpy

.. image:: https://coveralls.io/repos/github/aparrish/pronouncingpy/badge.svg?branch=master
        :target: https://coveralls.io/github/aparrish/pronouncingpy?branch=master

.. image:: https://img.shields.io/pypi/v/pronouncing.svg
        :target: https://pypi.python.org/pypi/pronouncing

Pronouncing is a simple interface for the CMU Pronouncing Dictionary. It's easy
to use and has no external dependencies. For example, here's how to find rhymes
for a given word::

    >>> import pronouncing
    >>> pronouncing.rhymes("climbing")
    ['diming', 'liming', 'priming', 'rhyming', 'timing']

Read the documentation here: https://pronouncing.readthedocs.org.

I made Pronouncing because I wanted to be able to use the CMU Pronouncing
Dictionary in my projects (and teach other people how to use it) without having
to install the grand behemoth that is NLTK.

Installation
------------

Install with pip like so::

    pip install pronouncing

You can also download the source code and install manually::

    python setup.py install

License
-------

The Python code in this module is distributed with a BSD license. A full copy
of the CMU Pronouncing Dictionary is included in this distribution. Learn
more about the CMU Pronouncing Dictionary here:
http://www.speech.cs.cmu.edu/cgi-bin/cmudict

Acknowledgements
----------------

This package was originally developed as part of my Spring 2015 research
fellowship at `ITP <http://itp.nyu.edu/itp/>`_. Thank you to the program and
its students for their interest and support!





History
=======

0.1.5 (2017-04-13)
------------------

* Messed up the PyPI upload. Yay!

0.1.4 (2017-04-12)
------------------

* Improved performance when retrieving rhyming words. (Based on pull request
  proposed by `WillPiledriver <https://github.com/WillPiledriver>`_.)


0.1.3 (2017-01-17)
------------------

* Various tweaks and performance improvements.


0.1.2 (2015-06-23)
------------------

* Pre-compiled regex for improved performance. (Contributed by John Wiseman.)

0.1.1 (2015-06-12)
---------------------

* First release on PyPI.


