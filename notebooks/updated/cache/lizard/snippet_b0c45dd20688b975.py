def _uncythonized_model(self, beta):
    parm = np.array([self.latent_variables.z_list[k].prior.transform(beta[k
        ]) for k in range(beta.shape[0])])
    model_scale, model_shape, model_skewness = self._get_scale_and_shape(parm)
    theta = np.matmul(self.X[self.integ + self.max_lag:], parm[self.sc +
        self.ar:self.sc + self.ar + len(self.X_names)])
    theta, self.model_scores = gasx_recursion(parm, theta, self.
        model_scores, self.model_Y, self.ar, self.sc, self.model_Y.shape[0],
        self.family.score_function, self.link, model_scale, model_shape,
        model_skewness, self.max_lag)
    return np.array(theta), self.model_Y, self.model_scores