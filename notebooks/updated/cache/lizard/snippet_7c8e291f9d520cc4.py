def adjoint(self):
    if not self.is_linear:
        raise OpNotImplementedError('nonlinear operators have no adjoint')
    return self.scalar.conjugate() * self.operator.adjoint