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


class TestGarland(unittest.TestCase):

    def test_absent_mock(self):
        self.assertIsInstance(examples.dictionary(), list)

    @garland.tinsel('tests.decorators.no_params', 'tests.examples')
    def test_decorated(self):
        self.assertIsInstance(examples.dictionary(), dict)

    def test_no_tinsel(self):
        """Ensure previous test mocking no longer functioning"""
        self.assertIsInstance(examples.dictionary(), list)


if __name__ == '__main__':
    unittest.main()
