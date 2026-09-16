def _get_jacobian_hessian_strategy(self):
    if self.jacobian is not None and self.hessian is None:
        jacobian = None
        hessian = 'cs'
    elif self.jacobian is None and self.hessian is None:
        jacobian = 'cs'
        hessian = soBFGS(exception_strategy='damp_update')
    else:
        jacobian = None
        hessian = None
    return jacobian, hessian