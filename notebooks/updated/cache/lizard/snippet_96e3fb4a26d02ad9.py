def _fill(self, direction, limit=None):
    if limit is None:
        limit = -1
    return self._get_cythonized_result('group_fillna_indexer', self.grouper,
        needs_mask=True, cython_dtype=np.int64, result_is_index=True,
        direction=direction, limit=limit)