def eval(self, n, signed=False):
    if self.is_empty:
        return []
    if self._reversed:
        return self._reverse().eval(n, signed=signed)
    results = []
    if self.stride == 0 and n > 0:
        results.append(self.lower_bound)
    else:
        if signed:
            bounds = self._signed_bounds()
        else:
            bounds = self._unsigned_bounds()
        for lb, ub in bounds:
            while len(results) < n and lb <= ub:
                results.append(lb)
                lb += self.stride
    return results