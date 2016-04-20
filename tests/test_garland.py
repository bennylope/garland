#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_garland
----------------------------------

Tests for `garland` module.
"""

import unittest
import garland

from . import examples
from . import examples as qualfied_examples


def dekorate(function):
    def wrapper(*args, **kwargs):
        return 90
    return wrapper


class TestFunctionDecoration(unittest.TestCase):
    """
    Basic testing and ensure that tests can be run with patching and without
    in sequence.
    """

    def test_absent_mock(self):
        self.assertIsInstance(examples.dictionary(), list)

    @garland.tinsel('tests.decorators.no_params', 'tests.examples')
    def test_decorated(self):
        self.assertIsInstance(examples.dictionary(), dict)

    def test_no_tinsel(self):
        """Ensure previous test mocking no longer functioning"""
        self.assertIsInstance(examples.dictionary(), list)

    @garland.tinsel('tests.decorators.with_params', 'tests.examples')
    def test_params(self):
        self.assertEqual(examples.world(), "world")

    @garland.tinsel('tests.decorators.with_params', 'tests.examples')
    def test_kwarg_params(self):
        self.assertEqual(examples.bar(), "bar")

    @garland.tinsel('tests.decorators.with_params', 'tests.examples')
    def test_qualified_import(self):
        self.assertEqual(qualfied_examples.bar(), "bar")

    @garland.tinsel('tests.decorators.no_params', 'tests.examples', dekorate)
    def test_decorated(self):
        """Ensure that custom mock decorators can be passed"""
        self.assertEqual(examples.dictionary(), 90)


class TestStackedDecorators(unittest.TestCase):

    def test_decoratored(self):
        self.assertEqual(examples.no_addition(4), 7)

    @garland.tinsel('tests.decorators.add_one', 'tests.examples')
    @garland.tinsel('tests.decorators.add_two', 'tests.examples')
    def test_remove_decorators(self):
        self.assertEqual(examples.no_addition(4), 4)


if __name__ == '__main__':
    unittest.main()
