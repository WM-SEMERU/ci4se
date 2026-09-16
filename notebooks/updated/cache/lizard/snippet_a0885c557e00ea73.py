def solve_minimize(self, func, weights, constraints, lower_bound=0.0,
    upper_bound=1.0, func_deriv=False):
    bounds = ((lower_bound, upper_bound),) * len(self.SUPPORTED_COINS)
    return minimize(fun=func, x0=weights, jac=func_deriv, bounds=bounds,
        constraints=constraints, method='SLSQP', options={'disp': False})