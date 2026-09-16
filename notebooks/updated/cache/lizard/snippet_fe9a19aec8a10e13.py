def coupl_model5(self):
    self.Coupl = -0.2 * self.Adj
    self.Coupl[2, 0] *= -1
    self.Coupl[3, 0] *= -1
    self.Coupl[4, 1] *= -1
    self.Coupl[5, 1] *= -1