def beta_hat(self):
    XKY = self.XKY()
    XanyKY = self.XanyKY()
    beta_hat, beta_hat_any = self.Areml_solver.solve(b_any=XanyKY, b=XKY,
        check_finite=True)
    return beta_hat, beta_hat_any