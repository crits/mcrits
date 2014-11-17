# List CRITs Indicators Metadata
# For use with mcrits
# Author: Brian Warehime @nulltr0n
# 11/14/2014

# Importing various modules

from MaltegoTransform import *
import requests
import json
import pprint

# Configuration Parser to grab necessary options.

#def getLocalConfPath():
#   	pathname = os.path.dirname(sys.argv[0])
#	pathname = os.path.abspath(pathname)
#	pathname = os.path.join(pathname, '..','local', 'munk.conf')
#	return os.path.normpath(pathname)

#configFile = getLocalConfPath()
#config = ConfigParser.SafeConfigParser()
#config.read(configFile)

#username = config.get('credentials', 'username')


# Setting up Maltego entities and getting initial variables.

me = MaltegoTransform()
me.parseArguments(sys.argv)
ioctype = sys.argv[1]
campaignname = me.getVar("campaign")

url = 'https://crits/api/v1/indicators/'
params = {
'api_key': '807d0b5f06ad21f3552691274e7ef73ccfa1cbd5',
'username': 'brian',
}
r = requests.get(url, params=params, verify=False)
j = json.loads(r.text)
for ioc in j['objects']:
	for value in ioc['campaign']:
		if value['name'] == campaignname and ioc['type'] == ioctype:
				ent = me.addEntity("mcrits.Indicator",ioc['value'])

# Return Maltego Output

me.returnOutput()