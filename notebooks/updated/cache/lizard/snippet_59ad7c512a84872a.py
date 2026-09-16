def get_identifiability_dataframe(self, singular_value=None, precondition=False
    ):
    if singular_value is None:
        singular_value = int(min(self.pst.nnz_obs, self.pst.npar_adj))
    xtqx = self.xtqx
    if precondition:
        xtqx = xtqx + self.parcov.inv
    v1_df = xtqx.v[:, :singular_value].to_dataframe() ** 2
    v1_df['ident'] = v1_df.sum(axis=1)
    return v1_df