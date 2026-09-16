def get_next(self, oid):
    try:
        self.lock.acquire()
        try:
            while len(oid) > 0 and oid[-2:] == '.0' and oid not in self.data:
                oid = oid[:-2]
            return self.get(self.data_idx[self.data_idx.index(oid) + 1])
        except ValueError:
            for real_oid in self.data_idx:
                if real_oid.startswith(oid):
                    return self.get(real_oid)
            return 'NONE'
        except IndexError:
            return 'NONE'
    finally:
        self.lock.release()