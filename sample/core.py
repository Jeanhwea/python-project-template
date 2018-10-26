# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

def hello():
  logger.info('hello world')
  return 'hello'
