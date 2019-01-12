# -*- coding: utf-8 -*-
__all__ = ()

# https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
