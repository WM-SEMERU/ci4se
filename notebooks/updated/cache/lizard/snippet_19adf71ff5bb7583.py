def surface_deriv(self, param):
    squeeze_out = np.shape(param) == ()
    param = np.array(param, dtype=float, copy=False, ndmin=1)
    if self.check_bounds and not is_inside_bounds(param, self.params):
        raise ValueError('`param` {} not in the valid range {}'.format(
            param, self.params))
    deriv = np.empty(param.shape + (2,))
    deriv[..., 0] = -np.sin(param)
    deriv[..., 1] = -np.cos(param)
    deriv *= self.radius
    deriv = np.matmul(deriv, np.transpose(self.rotation_matrix))
    if squeeze_out:
        deriv = deriv.squeeze()
    return deriv