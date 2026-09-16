def checkgrad(self, target_param=None, verbose=False, step=1e-06, tolerance
    =0.001, block_indices=None, plot=False):
    try:
        import numdifftools as nd
    except:
        raise ImportError(
            "Don't have numdifftools package installed, it is not a GPy dependency as of yet, it is only used for hessian tests"
            )
    if target_param:
        raise NotImplementedError(
            'Only basic functionality is provided with this gradchecker')
    current_index = 0
    for name, shape in zip(self.names, self.shapes):
        current_size = numpy.prod(shape)
        x = self.optimizer_array.copy()
        x = x[current_index:current_index + current_size].reshape(shape)
        analytic_hess = self._ddf(x)
        if analytic_hess.shape[1] == 1:
            analytic_hess = numpy.diagflat(analytic_hess)
        numeric_hess_partial = nd.Jacobian(self._df, vectorized=False)
        numeric_hess = numeric_hess_partial(x)
        check_passed = self.checkgrad_block(analytic_hess, numeric_hess,
            verbose=verbose, step=step, tolerance=tolerance, block_indices=
            block_indices, plot=plot)
        current_index += current_size
    return check_passed