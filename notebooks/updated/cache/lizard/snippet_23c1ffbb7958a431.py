def get_rel_path_fragment(self, doc_id):
    with self._index_lock:
        r = self._doc_index[doc_id]
    fp = r[-1]
    return fp[len(self.path) + 1:]