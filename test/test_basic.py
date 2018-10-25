# -*- coding: utf-8 -*-
import unittest

from sample.core import hello

class TestBasic(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello(), 'hello')
