def _get_site_amplification(self, sites, C):
    ssa, ssb, ssc, ssd, sse = self._get_site_type_dummy_variables(sites)
    return C['sA'] * ssa + C['sB'] * ssb + C['sC'] * ssc + C['sD'] * ssd + C[
        'sE'] * sse