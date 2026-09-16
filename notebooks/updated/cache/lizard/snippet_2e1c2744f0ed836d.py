def h_from_V(self, V, method='spline'):
    r
    if method == 'spline':
        if not self.table:
            self.set_table()
        return float(self.interp_h_from_V(V))
    elif method == 'chebyshev':
        if not self.chebyshev:
            self.set_chebyshev_approximators()
        return self.h_from_V_cheb(V)
    elif method == 'brenth':
        to_solve = lambda h: self.V_from_h(h, method='full') - V
        return brenth(to_solve, self.h_max, 0)
    else:
        raise Exception(
            "Allowable methods are 'full' or 'chebyshev', or 'brenth'.")