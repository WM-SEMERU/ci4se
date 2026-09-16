def free_shake(self, x):
    self.lock[:] = False
    normals, values, error = self._compute_equations(x)[:-1]
    counter = 0
    while True:
        if error <= self.threshold:
            break
        result = self._fast_shake(x, normals, values, error)
        counter += 1
        if result is not None:
            x, normals, values, error = result
        else:
            x, normals, values, error = self._rough_shake(x, normals,
                values, error)
            counter += 1
        if counter > self.max_iter:
            raise ConstraintError(
                'Exceeded maximum number of shake iterations.')
    return x, counter, len(values)