from hashuri.HashUriModule import HashUriModule
from hashuri.file import FileHasher

class FileModule(HashUriModule):
    def algorithm_id(self):
        return "FA"
    def is_correct_hash(self, content, hashstr):
        h = FileHasher.make_hash(content)
        return hashstr == h
