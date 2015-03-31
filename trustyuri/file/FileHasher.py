import hashlib
from trustyuri import TrustyUriUtils

def make_hash(content):
    return "FA" + TrustyUriUtils.get_base64(hashlib.sha256(content).digest())
