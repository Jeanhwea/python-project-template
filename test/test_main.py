# -*- coding: utf-8 -*-
import unittest

from sample.main import hello


class TestBasic(unittest.TestCase):

  def test_main(self):
    self.assertEqual(hello(), 'hello')
