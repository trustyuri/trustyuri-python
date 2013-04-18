import sys, HashUriUtils

filename = sys.argv[1]

print HashUriUtils.get_hashuri_datapart(filename)
