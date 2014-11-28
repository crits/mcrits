import os
import sys
import ConfigParser

from pycrits import pycrits

def get_crits():
    configFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),
                              '..', 'local', 'mcrits.conf')
    config = ConfigParser.SafeConfigParser()
    config.read(configFile)
    url = config.get('info', 'url')
    api_key = config.get('info', 'api_key')
    username = config.get('info', 'username')
    return pycrits(url, username, api_key)
