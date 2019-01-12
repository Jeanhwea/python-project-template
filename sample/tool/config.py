# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import yaml


def load_conifg(filename='custom.yml'):
  ''' load a yaml configuration file. '''
  if os.path.exists(filename):
    with open(filename, 'r') as yamlfile:
      return yaml.load(yamlfile)


def load_logging_config(filename='custom.yml'):
  ''' load logging config in "logging" section. '''
  config = load_conifg(filename)
  if 'logging' in config:
    return config['logging']
