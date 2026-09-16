def _get_mechanism(self, rup, coeffs):
    is_strike_slip = self.get_fault_type_dummy_variables(rup)
    return coeffs['b6'] * is_strike_slip