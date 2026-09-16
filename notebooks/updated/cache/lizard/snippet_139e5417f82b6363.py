def from_pandas_dataframe(cls, bqm_df, offset=0.0, interactions=None):
    if interactions is None:
        interactions = []
    bqm = cls({}, {}, offset, Vartype.BINARY)
    for u, row in bqm_df.iterrows():
        for v, bias in row.iteritems():
            if u == v:
                bqm.add_variable(u, bias)
            elif bias:
                bqm.add_interaction(u, v, bias)
    for u, v in interactions:
        bqm.add_interaction(u, v, 0.0)
    return bqm