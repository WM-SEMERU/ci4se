def prior_predictive_to_xarray(self):
    prior_predictive = self.prior_predictive
    if isinstance(prior_predictive, (tuple, list)) and prior_predictive[0
        ].endswith('.csv') or isinstance(prior_predictive, str
        ) and prior_predictive.endswith('.csv'):
        if isinstance(prior_predictive, str):
            prior_predictive = [prior_predictive]
        chain_data = []
        for path in prior_predictive:
            parsed_output = _read_output(path)
            for sample, *_ in parsed_output:
                chain_data.append(sample)
        data = _unpack_dataframes(chain_data)
    else:
        if isinstance(prior_predictive, str):
            prior_predictive = [prior_predictive]
        prior_predictive_cols = [col for col in self.prior[0].columns if
            any(item == col.split('.')[0] for item in prior_predictive)]
        data = _unpack_dataframes([item[prior_predictive_cols] for item in
            self.prior])
    return dict_to_dataset(data, coords=self.coords, dims=self.dims)