from MaltegoTransform import *
from mcrits_utils import *

crits = mcrits()

me = MaltegoTransform()
me.parseArguments(sys.argv)
id_ = me.getVar('id')
crits_type = me.getVar('crits_type')

for result in crits.get_related(crits_type, id_, 'Domain'):
    # For each related object, get the details.
    obj = crits.get_single_obj('Domain', result[1])
    ent = me.addEntity(result[0], obj['domain'])
    ent.addAdditionalFields(fieldName='id',
                            displayName='id',
                            value=result[1])

me.returnOutput()
