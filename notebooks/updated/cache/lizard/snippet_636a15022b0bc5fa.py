def clean(self):
    if self.pst_arg is None:
        self.logger.statement('linear_analysis.clean(): not pst object')
        return
    if not self.pst.estimation and self.pst.nprior > 0:
        self.drop_prior_information()