def save_checksum(self, path):
    checksum = file_hash(path)
    kv = unitdata.kv()
    kv.set('hardening:%s' % path, checksum)
    kv.flush()