# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging.config
from sample.tool.config import load_logging_config

logging.config.dictConfig(load_logging_config())
