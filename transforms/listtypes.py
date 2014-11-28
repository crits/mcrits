# List CRITs Indicator Types
# For use with mcrits
# Author: Brian Warehime @nulltr0n
# 11/14/2014

# Importing various modules

from MaltegoTransform import *
from mcrits_utils import get_crits

crits = get_crits()
me = MaltegoTransform()
campaignname = sys.argv[1]

params = { 'c-campaign.name': campaignname }

for batch in crits.indicators(params=params):
    for ioc in batch:
        if ioc['campaign'] == [] and campaignname == "Unknown":
            ent = me.addEntity("mcrits.Type", ioc['type'])
            ent.addAdditionalFields('campaign', 'campaign', '', campaignname)
            ent.addAdditionalFields('ioctype', 'ioctype', '', ioc['type'])
        else:
            for value in ioc['campaign']:
                if value['name'] == campaignname:
                    ent = me.addEntity("mcrits.Type", ioc['type'])
                    ent.addAdditionalFields('campaign', 'campaign', '', campaignname)
                    ent.addAdditionalFields('ioctype', 'ioctype', '', ioc['type'])

me.returnOutput()
