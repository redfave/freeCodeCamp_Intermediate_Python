import logging, traceback

try:
    a = 1,2,3
    value =a[4]
except Exception as e:
    logging.error(f'The error is {traceback.format_exc()}')
    # logging.error(e, exc_info=True)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s -\t%(name)s\t\t- %(levelname)s -\t\t%(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
import helper
logging.debug('This is a debug message')        # not displayed by default
logging.info('This is a info message')          # not displayed by default
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')

