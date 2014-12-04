from MaltegoTransform import *
from mcrits_utils import *

crits = mcrits()

me = MaltegoTransform()
me.parseArguments(sys.argv)
id_ = me.getVar('id')
crits_type = me.getVar('crits_type')

for result in crits.get_related(crits_type, id_, 'Indicator'):
    # For each related object, get the details.
    obj = crits.get_single_obj('Indicator', result[1])
    ent = me.addEntity(result[0], obj['value'])
    ent.addAdditionalFields(fieldName='id',
                            displayName='id',
                            value=result[1])
    ent.addAdditionalFields(fieldName='ind_type',
                            displayName='Indicator Type',
                            value=obj['type'])
    ent.addAdditionalFields(fieldName='value',
                            displayName='Indicator Value',
                            value=obj['value'])

me.returnOutput()
