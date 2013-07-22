from hashuri.HashUriModule import HashUriModule
from hashuri.rdf import RdfHasher, RdfUtils
from rdflib.graph import ConjunctiveGraph
from rdflib.util import guess_format

class RdfModule(HashUriModule):
    def algorithm_id(self):
        return "RA"
    def has_correct_hash(self, resource):
        f = guess_format(resource.get_filename(), {'xml': 'trix', 'ttl': 'turtle', 'nq': 'nquads', 'nt': 'nt'})
        cg = ConjunctiveGraph()
        cg.parse(data=resource.get_content(), format=f)
        quads = RdfUtils.get_quads(cg)
        h = RdfHasher.make_hash(quads, resource.get_hashstr())
        return resource.get_hashstr() == h
