def bitop_or(self, dest, key, *keys):
    return self.execute(b'BITOP', b'OR', dest, key, *keys)