import sys, os, re
from hashuri.file import FileHasher

filename = sys.argv[1]

with open (filename, "r") as f:
    hashstr = FileHasher.make_hash(f.read())
    ext = ""
    base = filename
    if re.search(r'.\.[A-Za-z0-9\-_]{0,20}$', filename):
        ext = re.sub(r'^(.*)(\.[A-Za-z0-9\-_]{0,20})$', r'\2', filename)
        base = re.sub(r'^(.*)(\.[A-Za-z0-9\-_]{0,20})$', r'\1', filename)
    os.rename(filename, base + "." + hashstr + ext)
