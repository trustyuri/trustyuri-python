import sys, logging, HashUriUtils, urllib2
from hashuri import ModuleDirectory
from hashuri.HashUriResource import HashUriResource

def check(args):
    filename = args[0]
    
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    args = sys.argv
    args.pop(0)
    check(args)
