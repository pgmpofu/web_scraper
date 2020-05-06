import logging
import os

def set_custom_log_info(filename):
    if  not os.path.exists(filename):
    filename = open('error.log', 'w+')
    else:
    logging.basicConfig(filename=filename, level=logging.INFO)

def report(e:Exception):
    logging.exception(str(e))