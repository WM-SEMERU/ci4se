def _process_monomial(self, monomial, n_vars):
    coeff, monomial = monomial.as_coeff_Mul()
    k = 0
    conjugate = False
    try:
        k = self.monomial_index[monomial]
    except KeyError:
        daggered_monomial = apply_substitutions(Dagger(monomial), self.
            substitutions, self.pure_substitution_rules)
        try:
            k = self.monomial_index[daggered_monomial]
            conjugate = True
        except KeyError:
            k = n_vars + 1
            self.monomial_index[monomial] = k
    if conjugate:
        k = -k
    return k, coeff