import hashlib
from trustyuri import TrustyUriUtils
from trustyuri.rdf.StatementComparator import StatementComparator
from rdflib.term import URIRef
import re
from trustyuri.rdf.RdfPreprocessor import preprocess

def make_hash(quads, hashstr=None):
    quads = preprocess(quads, hashstr=hashstr)
    comp = StatementComparator(hashstr)
    quads = sorted(quads, cmp=lambda q1, q2: comp.compare(q1, q2))
    s = ""
    for q in quads:
        s = s + value_to_string(q[0], hashstr)
        s = s + value_to_string(q[1], hashstr)
        s = s + value_to_string(q[2], hashstr)
        s = s + value_to_string(q[3], hashstr)
    # Uncomment next line to see what goes into the hash:
    #print "-----\n" + s + "-----\n"
    return "RA" + TrustyUriUtils.get_base64(hashlib.sha256(s).digest())

def value_to_string(value, hashstr):
    if value is None:
        return "\n"
    elif isinstance(value, URIRef):
        return value + "\n"
    else:
        if not value.language is None:
            return "@" + value.language + " " + escape(value) + "\n"
        if not value.datatype is None:
            return "^" + value.datatype + " " + escape(value) + "\n"
        return "^http://www.w3.org/2001/XMLSchema#string " + escape(value) + "\n"

def escape(s):
    return re.sub(r'\n', r'\\n', str(s))
