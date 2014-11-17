# List CRITs Indicators
# For use with mcrits
# Author: Brian Warehime @nulltr0n
# 11/14/2014

# Importing various modules

from MaltegoTransform import *
import requests
import json
import pprint
import re
import os
import ConfigParser

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
ioctype = me.getVar("ioctype")
campaignname = me.getVar("campaign")

# Setting up requests variables from mcrits.conf

url = url + '/api/v1/indicators/'
params = {
'api_key': api_key,
'username': username,
}

r = requests.get(url, params=params, verify=False)
j = json.loads(r.text)
for ioc in j['objects']:
	if ioc['campaign'] == [] and campaignname == "Unknown" and ioc['type'] == ioctype:
		ent = me.addEntity("mcrits.Indicator",ioc['value'])
	else:
		for value in ioc['campaign']:
			if value['name'] == campaignname and ioc['type'] == ioctype:
					ent = me.addEntity("mcrits.Indicator",ioc['value'])

# Return Maltego Output

me.returnOutput()