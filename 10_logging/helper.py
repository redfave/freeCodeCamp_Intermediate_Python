import  logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.propagate = False #propagation is on by default
logger.info('Hello from helper')

formatter = logging.Formatter('%(name)s -\t%(levelname)s -\t\t%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
file_handler = RotatingFileHandler('./10_logging/file.log', maxBytes=2000, backupCount=5)
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.warning(f'This is a warning from {__name__}')
logger.error(f'This is an error from {__name__}')

file_handler.setLevel(logging.CRITICAL)

for _ in range(10000):
    logger.critical('Fill the log')
