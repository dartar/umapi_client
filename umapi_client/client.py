"""

"""

__author__ = "ryan faulkner"
__email__ = 'rfaulkner@wikimedia.org'
__date__ = "2013-03-03"
__license__ = "GPL (version 2 or later)"

import twisted
from time import sleep
import multiprocessing as mp


def establish_connection():
    """
        Communicates with server
    """
    pass


def send_rsa():
    """
        Reads private key and transmits
    """
    pass


def send_requests():
    """
        Reads a file and sends urls sequentially
    """
    pass


def listener():
    while 1:
        sleep(1)
        #


if __name__ == '__main__':
    p = mp.Process(target=listener)
    p.start()
    p.join()

