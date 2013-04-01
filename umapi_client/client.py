"""
    Client for the Wikimedia foundation user metrics API.
"""

__author__ = "ryan faulkner"
__email__ = 'rfaulkner@wikimedia.org'
__date__ = "2013-03-03"
__license__ = "GPL (version 2 or later)"

from umapi_client import config

import json
import cookielib
import os
import urllib
import urllib2


class UMAPIClient(object):
    """
        Class wraps the login, cookie setting, and request functionality.
    """

    def __init__(self, login, password):
        """ Start up... """
        self.login = login
        self.password = password

        self.cj = cookielib.MozillaCookieJar(config.COOKIE_DIR +
                                             config.COOKIE_FILENAME)
        if os.access(config.COOKIE_DIR + config.COOKIE_FILENAME, os.F_OK):
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
