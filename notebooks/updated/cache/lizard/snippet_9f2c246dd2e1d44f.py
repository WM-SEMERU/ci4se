def _create_fit_summary(self):
    needed_attributes = ['df_model', 'nobs', 'null_log_likelihood',
        'log_likelihood', 'rho_squared', 'rho_bar_squared',
        'estimation_message']
    try:
        assert all([hasattr(self, attr) for attr in needed_attributes])
        assert all([(getattr(self, attr) is not None) for attr in
            needed_attributes])
    except AssertionError:
        msg = 'Call this function only after setting/calculating all other'
        msg_2 = ' estimation results attributes'
        raise NotImplementedError(msg + msg_2)
    self.fit_summary = pd.Series([self.df_model, self.nobs, self.
        null_log_likelihood, self.log_likelihood, self.rho_squared, self.
        rho_bar_squared, self.estimation_message], index=[
        'Number of Parameters', 'Number of Observations',
        'Null Log-Likelihood', 'Fitted Log-Likelihood', 'Rho-Squared',
        'Rho-Bar-Squared', 'Estimation Message'])
    return None