from hashuri.HashUriModule import HashUriModule
from hashuri.rdf import RdfHasher, RdfUtils
from rdflib.graph import ConjunctiveGraph

class RdfModule(HashUriModule):
    def algorithm_id(self):
        return "RA"
    def is_correct_hash(self, content, hashstr):
        cg = ConjunctiveGraph()
        cg.parse(data=content, format='trix')
        quads = RdfUtils.get_quads(cg)
        h = RdfHasher.make_hash(quads, hashstr)
        return hashstr == h
