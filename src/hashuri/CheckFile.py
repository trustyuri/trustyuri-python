import sys, HashUriUtils, urllib2
from hashuri import ModuleDirectory

filename = sys.argv[1]

datapart = HashUriUtils.get_hashuri_datapart(filename)
algorithm_id = datapart[:2]
module = ModuleDirectory.get_module(algorithm_id)
try:
    content = open(filename, 'r').read()
except:
    content = urllib2.urlopen(filename).read();
if module.is_correct_hash(content, datapart):
    print "Correct hash: " + datapart
else:
    print "*** INCORRECT HASH ***"
