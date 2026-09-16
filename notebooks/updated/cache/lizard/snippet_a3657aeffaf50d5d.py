def evalMetric(self, x, w1=None, w2=None):
    if w1 is None:
        w1 = self.w1
    if w2 is None:
        w2 = self.w2
    if self.verbose:
        print('----------')
        print('At design: ' + str(x))
    self._N_dv = len(_makeIter(x))
    if self.verbose:
        print('Evaluating surrogate')
    if self.surrogate is None:

        def fqoi(u):
            return self.fqoi(x, u)

        def fgrad(u):
            return self.jac(x, u)
        jac = self.jac
    else:
        fqoi, fgrad, surr_jac = self._makeSurrogates(x)
        jac = surr_jac
    u_samples = self._getParameterSamples()
    if self.verbose:
        print('Evaluating quantity of interest at samples')
    q_samples, grad_samples = self._evalSamples(u_samples, fqoi, fgrad, jac)
    if self.verbose:
        print('Evaluating metric')
    return self._evalWeightedSumMetric(q_samples, grad_samples)