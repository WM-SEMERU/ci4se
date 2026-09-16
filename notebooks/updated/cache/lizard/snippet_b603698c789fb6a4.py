def less_than_pi_constraints(self):
    pi = self.prior_information
    lt_pi = pi.loc[pi.apply(lambda x: self._is_less_const(x.obgnme) and x.
        weight != 0.0, axis=1), 'pilbl']
    return lt_pi