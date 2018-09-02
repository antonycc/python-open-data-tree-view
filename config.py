# Purpose: Logging config

# https://pypi.python.org/pypi/logmatic-python/0.1.7
# pip install logmatic-python

import logmatic
import sys
import logging


# Load configuration into globals


def initialise_logger(target_logger, level, logging_format, reset_handlers=False):
    if target_logger.hasHandlers() and reset_handlers:
        target_logger.handlers = []
    if level is not None:
        target_logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.NOTSET)
    target_logger.addHandler(handler)
    if logging_format == 'json':
        formatter = logmatic.JsonFormatter()
        handler.setFormatter(formatter)


def get_logger(name=sys.argv[0]):
    level = 'INFO'
    logging_format = 'text'
    named_logger = logging.getLogger(name)
    initialise_logger(named_logger, level, logging_format, True)
    return named_logger
