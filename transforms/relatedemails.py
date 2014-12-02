from MaltegoTransform import *
from mcrits_utils import *

crits = mcrits()

me = MaltegoTransform()
me.parseArguments(sys.argv)
id_ = me.getVar('id')
crits_type = me.getVar('crits_type')

for result in crits.get_related(crits_type, id_, 'Email'):
    # For each related object, get the details.
    obj = crits.get_single_obj('Email', result[1])
    ent = me.addEntity(result[0], result[1])
    ent.addAdditionalFields(fieldName='date',
                            displayName='Date',
                            value=obj['date'])
    ent.addAdditionalFields(fieldName='from',
                            displayName='From',
                            value=obj['from'])
    ent.addAdditionalFields(fieldName='subject',
                            displayName='subject',
                            value=obj['subject'])

me.returnOutput()
