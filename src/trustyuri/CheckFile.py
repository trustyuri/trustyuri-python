import sys, logging, TrustyUriUtils, urllib2
from trustyuri import ModuleDirectory
from trustyuri.TrustyUriResource import TrustyUriResource

def check(args):
    filename = args[0]
    
    tail = TrustyUriUtils.get_trustyuri_tail(filename)
    algorithm_id = tail[:2]
    module = ModuleDirectory.get_module(algorithm_id)
    try:
        content = open(filename, 'r').read()
    except:
        content = urllib2.urlopen(filename).read();
    resource = TrustyUriResource(filename, content, tail)
    if module.has_correct_hash(resource):
        print "Correct hash: " + tail
    else:
        print "*** INCORRECT HASH ***"

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    args = sys.argv
    args.pop(0)
    check(args)
