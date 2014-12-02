from MaltegoTransform import *
from mcrits_utils import *

crits = mcrits()

me = MaltegoTransform()
me.parseArguments(sys.argv)
id_ = me.getVar('id')
crits_type = me.getVar('crits_type')

# While rare, screenshots can actually be related to other objects.
for result in crits.get_related(crits_type, id_, 'Screenshot'):
    me.addEntity(result[0], result[1])

# They are more commonly stored as a list of IDs in a given object.
obj = crits.get_single_obj(crits_type, id_)
for screenshot in obj.get('screenshots', []):
    me.addEntity('mcrits.Screenshot', screenshot)

me.returnOutput()
