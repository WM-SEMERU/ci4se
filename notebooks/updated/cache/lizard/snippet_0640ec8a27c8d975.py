def _get_site_amplification(self, sites, rup, C):
    Sc, Sd = self._get_site_type_dummy_variables(sites)
    return (C['s11'] + C['s12'] * (rup.mag - 6.0)) * Sc + (C['s21'] + C[
        's22'] * (rup.mag - 6.0)) * Sd