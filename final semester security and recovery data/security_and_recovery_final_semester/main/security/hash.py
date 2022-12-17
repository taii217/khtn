import hashlib

def hash(key):
    return hashlib.md5(bytes(key, 'utf-8')).hexdigest()

