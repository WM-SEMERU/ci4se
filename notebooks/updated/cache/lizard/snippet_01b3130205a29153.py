def _extrapolate(self, result, v, below_bounds, above_bounds, der):
    if self.extrapolate_mode == 'const':
        fill_b = fill_a = self.fill_value
    elif self.extrapolate_mode == 'border':
        fill_b = self._poly_eval(0, 0, der)
        fill_a = self._poly_eval(0, -1, der)
    elif self.extrapolate_mode == 'extrapolate':
        u = v[above_bounds] - self._x[-2]
        fill_a = self._poly_eval(u, -2, der)
        u = v[below_bounds] - self._x[0]
        fill_b = self._poly_eval(u, 0, der)
    else:
        raise ValueError("extrapolation method doesn't exist")
    result[below_bounds] = fill_b
    result[above_bounds] = fill_a