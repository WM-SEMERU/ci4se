def get_errvar_dataframe(self, singular_values=None):
    if singular_values is None:
        singular_values = np.arange(0, min(self.pst.nnz_obs, self.pst.
            npar_adj) + 1)
    if not isinstance(singular_values, list) and not isinstance(singular_values
        , np.ndarray):
        singular_values = [singular_values]
    results = {}
    for singular_value in singular_values:
        sv_results = self.variance_at(singular_value)
        for key, val in sv_results.items():
            if key not in results.keys():
                results[key] = []
            results[key].append(val)
    return pd.DataFrame(results, index=singular_values)