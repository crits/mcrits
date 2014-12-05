import os
import sys
import ConfigParser

from pycrits import pycrits

class mcrits(object):
    def __init__(self):
        self.crits = self.get_crits()
        # Default string if no ID provided.
        self._NEED_ID = 'NEED ID'
        self._get_single_obj = {
                                 'Sample': self.crits.sample,
                                 'PCAP': self.crits.pcap,
                                 'Campaign': self.crits.campaign,
                                 'Indicator': self.crits.indicator,
                                 'Domain': self.crits.domain,
                                 'Event': self.crits.event,
                                 'Certificate': self.crits.certificate,
                                 'Email': self.crits.email,
                                 'IP': self.crits.ip,
                                 'RawData': self.crits.raw_data,
                                 'Screenshot': self.crits.screenshot,
                                 'Actor': self.crits.actor,
                                 'ActorIdentifier': self.crits.actor_identifier
                               }

        self._get_multi_obj = {
                                'Sample': self.crits.samples,
                                'PCAP': self.crits.pcaps,
                                'Campaign': self.crits.campaigns,
                                'Indicator': self.crits.indicators,
                                'Domain': self.crits.domains,
                                'Event': self.crits.events,
                                'Certificate': self.crits.certificates,
                                'Email': self.crits.emails,
                                'IP': self.crits.ips,
                                'RawData': self.crits.raw_datas,
                                'Screenshot': self.crits.screenshots,
                                'Actor': self.crits.actors,
                                'ActorIdentifier': self.crits.actor_identifier
                               }

    def get_crits(self):
        configFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),
                                  '..', 'local', 'mcrits.conf')
        config = ConfigParser.SafeConfigParser()
        config.read(configFile)
        url = config.get('info', 'url')
        api_key = config.get('info', 'api_key')
        username = config.get('info', 'username')
        verify = config.get('info', 'verify')
        crits = pycrits(url, username, api_key)
        if verify == 'False':
            crits.verify = False
        return crits

    def get_single_obj(self, crits_type, id_):
        func = self._get_single_obj.get(crits_type, None)
        if func == None:
            return {}
        return func(id_)

    def get_multi_obj(self, crits_type, params):
        func = self._get_multi_obj.get(crits_type, None)
        if func == None:
            return []
        return func(params=params)

    # crits_type is the type of the object to fetch.
    # id_ is the ID of the object to fetch.
    # type_ is the type of objects to get relationships for.
    # Return list of tuples [(mcrits.type_, ID)].
    def get_related(self, crits_type, id_, type_):
        results = []
        if id_ == self._NEED_ID:
            return results

        obj = self.get_single_obj(crits_type, id_)

        for relationship in obj.get('relationships', []):
            if relationship['type'] == type_:
                results.append(("mcrits.%s" % type_, relationship['value']))

        # If dealing with a campaign, walk the desired object type and find
        # all that are tagged with that campaign too. We already have the
        # campaign name in 'obj'. Do a search for all objects of desired
        # type tagged with that campaign.
        if crits_type == 'Campaign':
            params = {'c-campaign.name': obj['name']}
            for new_obj in self.get_multi_obj(type_, params):
                results.append(("mcrits.%s" % type_, new_obj['_id']))
        return results
