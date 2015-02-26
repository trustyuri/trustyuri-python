from rdflib.term import URIRef, BNode
import re
from rdflib.graph import ConjunctiveGraph, Graph
from rdflib.util import guess_format

def get_trustyuri_str(baseuri, hashstr, suffix=None):
    s = expand_baseuri(baseuri) + hashstr
    if not suffix is None:
        if suffix.startswith("."):
            # Make three dots, as two dots are reserved for blank nodes
            s = s + ".." + suffix
        else:
            s = s + "." + suffix
    return s

def get_trustyuri(resource, baseuri, hashstr, bnodemap):
    if resource is None:
        return None
    if isinstance(resource, URIRef):
        suffix = get_suffix(resource, baseuri)
        if suffix is None and not get_str(resource) == get_str(baseuri):
            return resource
        return URIRef(get_trustyuri_str(baseuri, hashstr, suffix))
    if isinstance(resource, BNode):
        n = get_bnode_number(resource, bnodemap)
        return URIRef(expand_baseuri(baseuri) + hashstr + ".." + str(n))
    else:
        return None

def get_suffix(plainuri, baseuri):
    p = get_str(plainuri)
    b = get_str(baseuri)
    if (p == b): return None
    if (p.startswith(b)): return p[len(b):]
    return None

def normalize(uri, hashstr):
    if hashstr is None: return get_str(uri)
    return re.sub(hashstr, " ", get_str(uri))

def get_bnode_number(bnode, bnodemap):
    i = get_str(bnode)
    if not bnodemap.has_key(i):
        n = len(bnodemap)+1
        bnodemap[i] = n
    return bnodemap[i]

def expand_baseuri(baseuri):
    s = get_str(baseuri)
    if re.match(r'.*[A-Za-z0-9\-_]', s): s = s + "."
    return s

def get_quads(conjunctivegraph):
    quads = []
    for s, p, o, c in conjunctivegraph.quads((None, None, None)):
        g = c.identifier
        if not isinstance(g, URIRef): g = None
        quads.append((g, s, p, o))
    return quads
    
def get_conjunctivegraph(quads):
    cg = ConjunctiveGraph()
#     for (c, s, p, o) in quads:
#         cg.default_context = Graph(store=cg.store, identifier=c)
#         cg.add((s, p, o))
    cg.addN([(s, p, o, Graph(store=cg.store, identifier=c)) for (c, s, p, o) in quads])
    return cg

def get_format(filename):
    return guess_format(filename, {'xml': 'trix', 'ttl': 'turtle', 'nq': 'nquads', 'nt': 'nt', 'rdf': 'xml'})

def get_str(s):
    return s.encode('utf-8')
