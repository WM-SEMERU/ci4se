def _model(self, beta):
    Y = np.array([reg[self.lags:reg.shape[0]] for reg in self.data])
    beta = np.array([self.latent_variables.z_list[k].prior.transform(beta[k
        ]) for k in range(beta.shape[0])])
    params = []
    col_length = 1 + self.ylen * self.lags
    for i in range(0, self.ylen):
        params.append(beta[col_length * i:col_length * (i + 1)])
    mu = np.dot(np.array(params), self._create_Z(Y))
    return mu, Y