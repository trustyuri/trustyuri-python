import hashlib
from hashuri import HashUriUtils
from rdflib.graph import ConjunctiveGraph
from hashuri.rdf.StatementComparator import StatementComparator
from rdflib.term import URIRef
import re

def make_hash(content, hashstr=None):
    if isinstance(content, ConjunctiveGraph):
        cg = content
    else:
        cg = ConjunctiveGraph();
        cg.parse(data=content, format='trix')
    quads = []
    for c in cg.contexts():
        for s, p, o in c:
            g = c.identifier
            if not isinstance(g, URIRef): g = None
            quads.append((g, s, p, o))
    quads = preprocess(quads, hashstr)
    comp = StatementComparator()
    quads = sorted(quads, cmp=lambda q1, q2: comp.compare(q1, q2))
    s = ""
    for q in quads:
        s = s + value_to_string(q[0], hashstr);
        s = s + value_to_string(q[1], hashstr);
        s = s + value_to_string(q[2], hashstr);
        s = s + value_to_string(q[3], hashstr);
    return "RA" + HashUriUtils.get_base64(hashlib.sha256(s).digest())

def preprocess(quads, hashstr):
    newquads = []
    for q in quads:
        c = transform(q[0], hashstr)
        s = transform(q[1], hashstr)
        p = transform(q[2], hashstr)
        o = q[3]
        if isinstance(q[3], URIRef):
            o = transform(q[3], hashstr)
        newquads.append((c, s, p, o));
    return newquads

def transform(uri, hashstr):
    if hashstr is None: return uri
    if uri is None: return None
    return URIRef(re.sub(hashstr, ' ', str(uri)))

def value_to_string(value, hashstr):
    if value is None:
        return "\n"
    elif isinstance(value, URIRef):
        return transform(value, hashstr) + "\n"
    else:
        if not value.datatype is None:
            return "^" + value.datatype + " " + escape(value) + "\n"
        if not value.language is None:
            return "@" + value.datatype + " " + escape(value) + "\n"
        return "#" + escape(value) + "\n"

def escape(s):
    return re.sub(r'\n', r'\\n', str(s))
