def execute(self, **minimize_options):
    minimizer_ans = self.minimizer.execute(**minimize_options)
    try:
        cov_matrix = minimizer_ans.covariance_matrix
    except AttributeError:
        cov_matrix = self.covariance_matrix(dict(zip(self.model.params,
            minimizer_ans._popt)))
    else:
        if cov_matrix is None:
            cov_matrix = self.covariance_matrix(dict(zip(self.model.params,
                minimizer_ans._popt)))
    finally:
        minimizer_ans.covariance_matrix = cov_matrix
    minimizer_ans.model = self.model
    minimizer_ans.gof_qualifiers['r_squared'] = r_squared(self.model,
        minimizer_ans, self.data)
    return minimizer_ans