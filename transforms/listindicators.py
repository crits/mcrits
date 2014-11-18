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

elems = ['_id','bucket_list','created','modified','sectors','status']

r = requests.get(url, params=params, verify=False)
j = json.loads(r.text)
for ioc in j['objects']:
	if ioc['campaign'] == [] and campaignname == "Unknown" and ioc['type'] == ioctype:
		if ioc['type'].startswith("Address"):
			ent = me.addEntity("mcrits.Address",ioc['value'])
		elif ioc['type'].startswith("DNS"):
			ent = me.addEntity("mcrits.DNS",ioc['value'])
		elif ioc['type'].startswith("Disk"):
			ent = me.addEntity("mcrits.Disk",ioc['value'])
		elif ioc['type'].startswith("Library"):
			ent = me.addEntity("mcrits.Library",ioc['value'])
		elif ioc['type'].startswith("Network"):
			ent = me.addEntity("mcrits.Network",ioc['value'])
		elif ioc['type'].startswith("URI"):
			ent = me.addEntity("mcrits.URI",ioc['value'])
		elif ioc['type'].startswith("Win"):
			ent = me.addEntity("mcrits.Windows",ioc['value'])
		else:
			ent = me.addEntity("mcrits.Indicator",ioc['value'])
		for elem in elems:
			if ioc[elem] == []:
				pass
			else:
				if len(ioc[elem][0]) == 1:
					ent.addAdditionalFields(elem, elem,'',ioc[elem])
				else:
					ent.addAdditionalFields(elem, elem,'',ioc[elem][0])
					ent.addAdditionalFields('confidence','confidence','',ioc['confidence']['rating'])
					ent.addAdditionalFields('impact','impact','',ioc['impact']['rating'])
					ent.addAdditionalFields('source','source','',ioc['source'][0]['name'])
					ent.addAdditionalFields('campaign', 'campaign','',campaignname)
	else:
		for value in ioc['campaign']:
			if value['name'] == campaignname and ioc['type'] == ioctype:
				if ioc['type'].startswith("Address"):
					ent = me.addEntity("mcrits.Address",ioc['value'])
				elif ioc['type'].startswith("DNS"):
					ent = me.addEntity("mcrits.DNS",ioc['value'])
				elif ioc['type'].startswith("Disk"):
					ent = me.addEntity("mcrits.Disk",ioc['value'])
				elif ioc['type'].startswith("Library"):
					ent = me.addEntity("mcrits.Library",ioc['value'])
				elif ioc['type'].startswith("Network"):
					ent = me.addEntity("mcrits.Network",ioc['value'])
				elif ioc['type'].startswith("URI"):
					ent = me.addEntity("mcrits.URI",ioc['value'])
				elif ioc['type'].startswith("Win"):
					ent = me.addEntity("mcrits.Windows",ioc['value'])
				else:
					ent = me.addEntity("mcrits.Indicator",ioc['value'])
				# Add additional fields to entity
				for elem in elems:
					if ioc[elem] == []:
						pass
					else:
						if len(ioc[elem][0]) == 1:
							ent.addAdditionalFields(elem, elem,'',ioc[elem])
						else:
							ent.addAdditionalFields(elem, elem,'',ioc[elem][0])
							ent.addAdditionalFields('confidence','confidence','',ioc['confidence']['rating'])
							ent.addAdditionalFields('impact','impact','',ioc['impact']['rating'])
							ent.addAdditionalFields('source','source','',ioc['source'][0]['name'])
							ent.addAdditionalFields('campaign', 'campaign','',campaignname)

me.returnOutput()