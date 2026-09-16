def get_design_matrix(self, names=None, format='long', mode='both', force=
    False, sampling_rate='TR', **kwargs):
    sparse_df, dense_df = None, None
    coll = self.collection
    if self.level != 'run' and mode != 'sparse':
        mode = 'sparse'
    include_sparse = include_dense = force and mode != 'both'
    if mode in ['sparse', 'both']:
        kwargs['sparse'] = True
        sparse_df = coll.to_df(names, format, include_dense=include_dense,
            **kwargs)
    if mode in ['dense', 'both']:
        kwargs['timing'] = True
        kwargs['sparse'] = False
        if sampling_rate == 'TR':
            trs = {var.run_info[0].tr for var in self.collection.variables.
                values()}
            if not trs:
                raise ValueError(
                    'Repetition time unavailable; specify sampling_rate explicitly'
                    )
            elif len(trs) > 1:
                raise ValueError(
                    'Non-unique Repetition times found ({!r}); specify sampling_rate explicitly'
                    )
            sampling_rate = 1.0 / trs.pop()
        elif sampling_rate == 'highest':
            sampling_rate = None
        dense_df = coll.to_df(names, format='wide', include_sparse=
            include_sparse, sampling_rate=sampling_rate, **kwargs)
        if dense_df is not None:
            dense_df = dense_df.drop(['onset', 'duration'], axis=1)
    return DesignMatrixInfo(sparse_df, dense_df, self.entities)