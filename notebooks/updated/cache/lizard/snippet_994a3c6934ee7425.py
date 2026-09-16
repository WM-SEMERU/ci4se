def sdiffstore(self, destkey, key, *keys):
    return self.execute(b'SDIFFSTORE', destkey, key, *keys)