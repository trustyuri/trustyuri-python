import hashlib
from hashuri import HashUriUtils

def make_hash(content):
    return "FA" + HashUriUtils.get_base64(hashlib.sha256(content).digest())
