def train(self, ds):
    if self.useErrors:
        (self.coeffs, self.scatters, self.new_tr_labels, self.chisqs, self.
            pivots, self.scales) = _train_model_new(ds)
    else:
        (self.coeffs, self.scatters, self.chisqs, self.pivots, self.scales
            ) = _train_model(ds)