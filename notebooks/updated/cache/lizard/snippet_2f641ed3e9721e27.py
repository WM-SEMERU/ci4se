def zeroed(self, tol=0.001):
    new_tensor = self.copy()
    new_tensor[abs(new_tensor) < tol] = 0
    return new_tensor