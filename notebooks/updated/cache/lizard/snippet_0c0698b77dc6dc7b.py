def set_params(self, **params):
    if 'theta' in params and params['theta'] != self.theta:
        raise ValueError('Cannot update theta. Please create a new graph')
    if 'anisotropy' in params and params['anisotropy'] != self.anisotropy:
        raise ValueError('Cannot update anisotropy. Please create a new graph')
    if 'kernel_symm' in params and params['kernel_symm'] != self.kernel_symm:
        raise ValueError('Cannot update kernel_symm. Please create a new graph'
            )
    super().set_params(**params)
    return self