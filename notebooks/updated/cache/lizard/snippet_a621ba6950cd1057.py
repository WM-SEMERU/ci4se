def compute_residuals(self):
    r = self.rsdl()
    adapt_tol = self.opt['RelStopTol']
    if self.opt['AutoStop', 'Enabled']:
        adapt_tol = self.tau0 / (1.0 + self.k)
    return r, adapt_tol