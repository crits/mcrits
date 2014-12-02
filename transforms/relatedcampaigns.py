from MaltegoTransform import *
from mcrits_utils import *

crits = mcrits()

me = MaltegoTransform()
me.parseArguments(sys.argv)
id_ = me.getVar('id')
crits_type = me.getVar('crits_type')

if id_ == crits._NEED_ID:
    me.returnOutput()

# Because we can get campaigns from two places (tagged vs related)
# we need to store the mapping of id to name to make sure we don't
# create two entities for the same campaign if both tagged and related.
campaigns = {}

# Campaigns can be used to tag objects, but also related to an object.
# The loop walks each campaign this object is tagged with and fetches the
# campaign object from crits via name. If the name and id are not in the
# dictionary create an entity for it.
obj = crits.get_single_obj(crits_type, id_)
for campaign in obj.get('campaign', []):
    # Should only ever be one of these.
    campaign_obj = crits.crits.campaign_by_name(campaign['name'])[0]
    if (campaign['name'] in campaigns and
        campaigns[campaign['name']] == campaign_obj['_id']):
        # Repeat campaign, skip it.
        continue

    campaigns[campaign['name']] = campaign_obj['_id']

    ent = me.addEntity('mcrits.Campaign', campaign['name'])
    ent.addAdditionalFields(fieldName='id',
                            displayName=campaign_obj['_id'],
                            value=campaign_obj['_id'])

# This loop is the inverse of the above. For each related campaign use the
# id to get the name.
for result in crits.get_related(crits_type, id_, 'Campaign'):
    # For each related Campaign, get the name.
    campaignname = crits.crits.campaign(result[1])['name']
    if (campaignname in campaigns and
        campaigns[campaignname] == result[1]):
        # Repeat campaign, skip it.
        continue

    campaigns[campaignname] = result[1]

    ent = me.addEntity(result[0], campaignname)
    ent.addAdditionalFields(fieldName='id',
                            displayName=result[1],
                            value=result[1])

me.returnOutput()
