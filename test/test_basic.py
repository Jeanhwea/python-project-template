# -*- coding: utf-8 -*-
import unittest
import logging.config

from sample.core import hello

logging.config.fileConfig('logging.conf')

class TestBasic(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello(), 'hello')
