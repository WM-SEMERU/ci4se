def _compute_magnitude_scaling(self, rup, C):
    U, SS, NS, RS = self._get_fault_type_dummy_variables(rup)
    if rup.mag <= C['Mh']:
        return C['e1'] * U + C['e2'] * SS + C['e3'] * NS + C['e4'] * RS + C[
            'e5'] * (rup.mag - C['Mh']) + C['e6'] * (rup.mag - C['Mh']) ** 2
    else:
        return C['e1'] * U + C['e2'] * SS + C['e3'] * NS + C['e4'] * RS + C[
            'e7'] * (rup.mag - C['Mh'])