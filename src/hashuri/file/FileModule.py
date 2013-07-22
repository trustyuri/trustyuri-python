from hashuri.HashUriModule import HashUriModule
from hashuri.file import FileHasher

class FileModule(HashUriModule):
    def algorithm_id(self):
        return "FA"
    def has_correct_hash(self, resource):
        h = FileHasher.make_hash(resource.get_content())
        return resource.get_hashstr() == h
