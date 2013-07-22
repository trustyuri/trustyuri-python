import sys, logging
from rdflib.graph import ConjunctiveGraph
from hashuri.rdf import RdfUtils, RdfTransformer
from rdflib.term import URIRef
import os

logging.basicConfig(level=logging.ERROR)

filename = sys.argv[1]
infile = file(filename)
baseuristr = sys.argv[2]

with open (filename, "r") as f:
    rdfFormat = RdfUtils.get_format(filename)
    cg = ConjunctiveGraph()
    cg.parse(data=f.read(), format=rdfFormat)
    quads = RdfUtils.get_quads(cg)
    baseuri = URIRef(baseuristr)
    outdir = os.path.abspath(os.path.join(str(file), os.pardir))
    RdfTransformer.transform_to_file(cg, baseuri, outdir, filename)
