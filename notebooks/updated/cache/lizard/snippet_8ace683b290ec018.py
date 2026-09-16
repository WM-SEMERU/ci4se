def reference_index(self):
    if self._db_location:
        ref_indices = glob.glob(os.path.join(self._db_location, '*', self.
            _REF_INDEX))
        if ref_indices:
            return ref_indices[0]