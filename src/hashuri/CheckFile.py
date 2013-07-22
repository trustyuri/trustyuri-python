import sys, logging, HashUriUtils, urllib2
from hashuri import ModuleDirectory
from hashuri.HashUriResource import HashUriResource

logging.basicConfig(level=logging.ERROR)

filename = sys.argv[1]

datapart = HashUriUtils.get_hashuri_datapart(filename)
algorithm_id = datapart[:2]
module = ModuleDirectory.get_module(algorithm_id)
try:
    content = open(filename, 'r').read()
except:
    content = urllib2.urlopen(filename).read();
resource = HashUriResource(filename, content, datapart)
if module.has_correct_hash(resource):
    print "Correct hash: " + datapart
else:
    print "*** INCORRECT HASH ***"
