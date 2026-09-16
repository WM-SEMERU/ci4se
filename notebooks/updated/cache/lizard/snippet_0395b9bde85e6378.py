def prior_predictive_to_xarray(self):
    prior = self.prior
    prior_model = self.prior_model
    prior_predictive = self.prior_predictive
    data = get_draws_stan3(prior, model=prior_model, variables=prior_predictive
        )
    return dict_to_dataset(data, library=self.stan, coords=self.coords,
        dims=self.dims)