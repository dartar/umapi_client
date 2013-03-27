"""
    Client for the Wikimedia foundation user metrics API.
"""

__author__ = "ryan faulkner"
__email__ = 'rfaulkner@wikimedia.org'
__date__ = "2013-03-03"
__license__ = "GPL (version 2 or later)"

from umapi_client import config, logging

from sys import exit
import json
import cookielib
import os
import urllib
import urllib2


class UMAPIRequester(object):
    """
        Class wraps the login, cookie setting, and request functionality.
    """

    def __init__(self, login, password):
        """ Start up... """
        self.login = login
        self.password = password

        self.cj = cookielib.MozillaCookieJar(config.COOKIE_FILENAME)
        if os.access(config.COOKIE_FILENAME, os.F_OK):
            self.cj.load()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                            'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        # need this twice - once to set cookies, once to log in...
        self.umapi_login()
        self.umapi_login()

        self.cj.save()

    def umapi_login(self):
        """
            Handle login. This should populate our cookie jar.
        """
        login_data = urllib.urlencode({
            'username': self.login,
            'password': self.password,
            'remember': 'yes'
        })
        response = self.opener.open(config.URL_ROOT + 'login', login_data)
        return ''.join(response.readlines())

    def get_request(self, url):
        response = self.opener.open(url)
        return json.dumps(''.join(response.readlines()))


def main():
    url = 'cohorts/ryan_test_2/bytes_added'

    # Initialize a requester object
    umapi_req = UMAPIRequester(config.UMAPI_USER,
                               config.UMAPI_PASS)

    # Make request
    try:
        response = umapi_req.get_request(config.URL_ROOT + url)
    except Exception as e:
        logging.error(__name__ + ' :: Bad response - {0}.'.format(e.message))
        return

    print str(json.loads(response))


def cli():
    exit(main())


if __name__ == '__main__':
    cli()


