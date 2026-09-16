def finalize(self):
    prehashed_digest = self._hasher.finalize()
    return _ecc_static_length_signature(key=self.key, algorithm=self.
        algorithm, digest=prehashed_digest)