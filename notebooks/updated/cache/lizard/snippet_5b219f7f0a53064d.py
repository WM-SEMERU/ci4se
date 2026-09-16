def nprior(self):
    self.control_data.nprior = self.prior_information.shape[0]
    return self.control_data.nprior