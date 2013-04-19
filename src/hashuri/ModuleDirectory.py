from hashuri.file.FileModule import FileModule
from hashuri.rdf.RdfModule import RdfModule

modules = {}

def add_module(module):
    modules[module.algorithm_id()] = module

def get_module(name):
    return modules[name]

add_module(FileModule())
add_module(RdfModule())
