# List CRITs Actors
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

# Setting up requests variables from mcrits

url = url + '/api/v1/actors/'
params = {
'api_key': api_key,
'username': username,
}

elems = ['_id','aliases','created','modified','description','sectors','status']

r = requests.get(url, params=params, verify=False)
j = json.loads(r.text)
for actor in j['objects']:
	if actor['campaign'] == [] and campaignname == "Unknown":
		ent = me.addEntity("mcrits.Actor",actor['name'] + "\r\n(" + campaignname + ")")
		for elem in elems:
			if actor[elem] == []:
				pass
			else:
				if len(actor[elem][0]) == 1:
					ent.addAdditionalFields(elem, elem,'',actor[elem])
				else:
					ent.addAdditionalFields(elem, elem,'',actor[elem][0])
					ent.addAdditionalFields('source','source','',actor['source'][0]['name'])
					ent.addAdditionalFields('campaign', 'campaign','',campaignname)
	else:
		for value in actor['campaign']:
			if value['name'] == campaignname:
				ent = me.addEntity("mcrits.Actor",actor['name'] + "\r\n(" + campaignname + ")")
				for elem in elems:
					if actor[elem] == []:
						pass
					else:
						if len(actor[elem][0]) == 1:
							#print actor[elem][0]
							ent.addAdditionalFields(elem, elem,'',actor[elem])
						else:
							ent.addAdditionalFields(elem, elem,'',actor[elem][0])
							ent.addAdditionalFields('source','source','',actor['source'][0]['name'])
							ent.addAdditionalFields('campaign', 'campaign','',campaignname)

# Return Maltego Output

me.returnOutput()