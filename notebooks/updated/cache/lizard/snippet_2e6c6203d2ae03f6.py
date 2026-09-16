def delete(self, key):
    with self._lmdb.begin(write=True, buffers=True) as txn:
        txn.delete(key.encode())