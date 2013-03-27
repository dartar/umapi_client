
import logging
import sys

TIMESTAMP_FORMAT = "%Y%m%d%H%M%S"
RESPONSE_FORMAT = '.json'

logging.basicConfig(level=logging.DEBUG, stream=sys.stderr,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%b-%d %H:%M:%S')