def prior_predictive_to_xarray(self):
    prior = self.prior
    prior_predictive = self.prior_predictive
    data = get_draws(prior, variables=prior_predictive)
    return dict_to_dataset(data, library=self.pystan, coords=self.coords,
        dims=self.dims)