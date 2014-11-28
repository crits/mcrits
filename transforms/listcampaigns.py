# List CRITs Campaigns
# For use with mcrits
# Author: Brian Warehime @nulltr0n
# 11/14/2014

from MaltegoTransform import *
from mcrits_utils import get_crits

crits = get_crits()

me = MaltegoTransform()

for batch in crits.campaigns():
    for campaign in batch:
        ent = me.addEntity("mcrits.Campaign", campaign['name'])

ent = me.addEntity("mcrits.Campaign", 'Unknown')
me.returnOutput()
