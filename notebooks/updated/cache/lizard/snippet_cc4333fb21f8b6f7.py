def read_md5(self, hex=False):
    f = self.open('rb')
    try:
        m = hashlib.md5()
        while True:
            d = f.read(8192)
            if not d:
                break
            m.update(d)
    finally:
        f.close()
    if hex:
        return m.hexdigest()
    else:
        return m.digest()