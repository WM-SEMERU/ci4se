def _get_facvar(self, polynomial):
    facvar = [0] * (self.n_vars + 1)
    if is_number_type(polynomial):
        facvar[0] = polynomial
        return facvar
    polynomial = polynomial.expand()
    if polynomial.is_Mul:
        elements = [polynomial]
    else:
        elements = polynomial.as_coeff_mul()[1][0].as_coeff_add()[1]
    for element in elements:
        results = self._get_index_of_monomial(element)
        for k, coeff in results:
            facvar[k] += coeff
    return facvar