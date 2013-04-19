import hashlib
from hashuri import HashUriUtils
from hashuri.rdf.StatementComparator import StatementComparator
from rdflib.term import URIRef
import re
from hashuri.rdf.RdfPreprocessor import preprocess

def make_hash(quads, hashstr=None):
    quads = preprocess(quads, hashstr=hashstr)
    comp = StatementComparator(hashstr)
    quads = sorted(quads, cmp=lambda q1, q2: comp.compare(q1, q2))
    s = ""
    for q in quads:
        s = s + value_to_string(q[0], hashstr);
        s = s + value_to_string(q[1], hashstr);
        s = s + value_to_string(q[2], hashstr);
        s = s + value_to_string(q[3], hashstr);
    return "RA" + HashUriUtils.get_base64(hashlib.sha256(s).digest())

def value_to_string(value, hashstr):
    if value is None:
        return "\n"
    elif isinstance(value, URIRef):
        return value + "\n"
    else:
        if not value.datatype is None:
            return "^" + value.datatype + " " + escape(value) + "\n"
        if not value.language is None:
            return "@" + value.datatype + " " + escape(value) + "\n"
        return "#" + escape(value) + "\n"

def escape(s):
    return re.sub(r'\n', r'\\n', str(s))
