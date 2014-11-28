# List CRITs Indicators
# For use with mcrits
# Author: Brian Warehime @nulltr0n
# 11/14/2014

from MaltegoTransform import *
from mcrits_utils import get_crits

def addentities(ioc):
    global me

    #Maltego Entities
    if ioc['type'] == "Address - ipv4-addr":
        ent = me.addEntity("maltego.IPv4Address", ioc['value'])
    elif ioc['type'] == "Address - e-mail":
        ent = me.addEntity("maltego.EmailAddress", ioc['value'])
    elif ioc['type'] == "URI - Domain Name":
        ent = me.addEntity("maltego.Domain", ioc['value'])
    elif ioc['type'] == "URI - URL":
        ent = me.addEntity("maltego.URL", ioc['value'])
    elif ioc['type'] == "Network Subnet" or ioc['type'] == "Address - cidr" or ioc['type'] == "Address - ipv4-net":
        ent = me.addEntity("maltego.Netblock", ioc['value'])

    #mcrits Specific Entities
    elif ioc['type'].startswith("Disk"):
        ent = me.addEntity("mcrits.Disk", ioc['value'])
    elif ioc['type'].startswith("Library"):
        ent = me.addEntity("mcrits.Library", ioc['value'])
    elif ioc['type'].startswith("Win"):
        ent = me.addEntity("mcrits.Windows", ioc['value'])
    else:
        ent = me.addEntity("mcrits.Indicator", ioc['value'])

    for elem in ['_id', 'bucket_list', 'created', 'modified', 'sectors', 'status']:
        if ioc[elem] != []:
            if len(ioc[elem][0]) == 1:
                ent.addAdditionalFields(elem, elem, '', ioc[elem])
            else:
                ent.addAdditionalFields(elem, elem, '', ioc[elem][0])
                ent.addAdditionalFields('confidence', 'confidence', '', ioc['confidence']['rating'])
                ent.addAdditionalFields('impact', 'impact', '', ioc['impact']['rating'])
                ent.addAdditionalFields('source', 'source', '', ioc['source'][0]['name'])
                ent.addAdditionalFields('campaign', 'campaign', '', campaignname)

me = MaltegoTransform()
me.parseArguments(sys.argv)
ioctype = me.getVar("ioctype")
campaignname = me.getVar("campaign")

crits = get_crits()

params = { 'c-campaign.name': campaignname, 'c-type': ioctype }

for batch in crits.indicators(params=params):
    for ioc in batch:
        if ioc['campaign'] == [] and campaignname == "Unknown":
            ioc['campaign'] = [{'name': campaignname}]

        for value in ioc['campaign']:
            if value['name'] == campaignname:
                addentities(ioc)

me.returnOutput()
