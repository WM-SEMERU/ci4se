def directional_poisson_ratio(self, n, m, tol=1e-08):
    n, m = get_uvec(n), get_uvec(m)
    if not np.abs(np.dot(n, m)) < tol:
        raise ValueError('n and m must be orthogonal')
    v = self.compliance_tensor.einsum_sequence([n] * 2 + [m] * 2)
    v *= -1 / self.compliance_tensor.einsum_sequence([n] * 4)
    return v