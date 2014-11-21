# List CRITs Indicator Types
# For use with mcrits
# Author: Brian Warehime @nulltr0n
# 11/14/2014

# Importing various modules

from MaltegoTransform import *
import requests
import json
import pprint
import sys
import ConfigParser
import os

# Configuration Parser to grab necessary options.

def getLocalConfPath():
    pathname = os.path.dirname(sys.argv[0])
    pathname = os.path.abspath(pathname)
    pathname = os.path.join(pathname, '..','local', 'mcrits.conf')
    return os.path.normpath(pathname)

configFile = getLocalConfPath()
config = ConfigParser.SafeConfigParser()
config.read(configFile)

username = config.get('info', 'username')
url = config.get('info', 'url')
api_key = config.get('info', 'api_key')

# Setting up Maltego entities and getting initial variables.

me = MaltegoTransform()
me.parseArguments(sys.argv)
campaignname = sys.argv[1]

# Setting up requests variables from mcrits.conf

url = url + '/api/v1/indicators/'
params = {
'api_key': api_key,
'username': username,
'c-campaign.name': campaignname,
'limit': '100'
}

r = requests.get(url, params=params, verify=False)
j = json.loads(r.text)
for ioc in j['objects']:
    if ioc['campaign'] == [] and campaignname == "Unknown":
        ent = me.addEntity("mcrits.Type",ioc['type'] + "\r\n(" + campaignname + ")")
        ent.addAdditionalFields('campaign', 'campaign','',campaignname)
        ent.addAdditionalFields('ioctype', 'ioctype','',ioc['type'])
    else:
        for value in ioc['campaign']:
            if value['name'] == campaignname:
                ent = me.addEntity("mcrits.Type",ioc['type'] + "\r\n(" + campaignname + ")")
                ent.addAdditionalFields('campaign', 'campaign','',campaignname)
                ent.addAdditionalFields('ioctype', 'ioctype','',ioc['type'])

# Return Maltego Output

me.returnOutput()