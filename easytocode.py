import sys
filedata = open('silly.input','rb').read()
 
FORBIDDEN_STRINGS = ['import', '.', '_', 'class', '>>', 'exec', 'assert','@','lambda','<<','slice','yield','try','except','global']

for forbidden_string in FORBIDDEN_STRINGS:
  if forbidden_string in filedata:
    print 'Cannot have "'+forbidden_string+'" in program.'
    sys.exit(1)

namespace = {}
namespace['__builtins__'] = {'False':False, 'True':True, 'None':None}

exec filedata in namespace
