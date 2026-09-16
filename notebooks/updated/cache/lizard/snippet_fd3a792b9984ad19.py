def transform(self, X):
    self._validate()
    Xt, Xc = get_ts_data_parts(X)
    check_array(Xt, dtype='numeric', ensure_2d=False, allow_nd=True)
    fts = np.column_stack([trans.transform(self._select(Xt, cols)) for _,
        trans, cols in self.transformers])
    if Xc is not None:
        fts = np.column_stack([fts, Xc])
    return fts