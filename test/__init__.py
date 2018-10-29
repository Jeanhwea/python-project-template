# -*- coding: utf-8 -*-
import logging.config
import os
import sys

logging.config.fileConfig('logging.conf')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
