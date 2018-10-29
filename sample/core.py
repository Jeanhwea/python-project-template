# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

def hello():
  logger.debug('debug message')
  logger.info('info message')
  logger.warning  ('warn message')
  logger.error('error message')
  logger.critical('critical message')
  return 'hello'
