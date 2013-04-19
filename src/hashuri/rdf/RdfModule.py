from hashuri.HashUriModule import HashUriModule
from hashuri.rdf import RdfHasher

class RdfModule(HashUriModule):
    def algorithm_id(self):
        return "RA"
    def is_correct_hash(self, content, hashstr):
        h = RdfHasher.make_hash(content, hashstr)
        return hashstr == h
