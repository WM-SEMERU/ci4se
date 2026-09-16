def eval_llk(self, input_df, full_llk=False):
    assert self.is_fitted
    self._process_valset(input_df, valset=False)
    self.ncores = cython_loops.cast_int(self.ncores)
    out = {'llk': cython_loops.calc_llk(self.val_set.Count.values, self.
        val_set.UserId.values, self.val_set.ItemId.values, self.Theta, self
        .Beta, self.k, self.ncores, cython_loops.cast_int(bool(full_llk))),
        'nobs': self.val_set.shape[0]}
    del self.val_set
    return out