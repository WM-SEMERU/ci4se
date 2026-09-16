def calc_next_ma_coef(self, ma_order, ma_model):
    idx = ma_order - 1
    coef = ma_model.coefs[idx]
    for jdx, ar_coef in enumerate(self.ar_coefs):
        zdx = idx - jdx - 1
        if zdx >= 0:
            coef -= ar_coef * ma_model.coefs[zdx]
    self.ma_coefs = numpy.concatenate((self.ma_coefs, [coef]))