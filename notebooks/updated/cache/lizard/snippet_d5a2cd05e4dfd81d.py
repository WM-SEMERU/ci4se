def ppc(self, nsims=1000, T=np.mean):
    if self.latent_variables.estimation_method not in ['BBVI', 'M-H']:
        raise Exception('No latent variables estimated!')
    else:
        lv_draws = self.draw_latent_variables(nsims=nsims)
        sigmas = [self._model(lv_draws[:, (i)])[0] for i in range(nsims)]
        data_draws = np.array([fam.Skewt.draw_variable(loc=self.
            latent_variables.z_list[-2].prior.transform(lv_draws[-2, i]),
            shape=self.latent_variables.z_list[-3].prior.transform(lv_draws
            [-3, i]), skewness=self.latent_variables.z_list[-4].prior.
            transform(lv_draws[-4, i]), nsims=len(sigmas[i]), scale=np.exp(
            sigmas[i] / 2.0)) for i in range(nsims)])
        T_sims = T(self.sample(nsims=nsims), axis=1)
        T_actual = T(self.data)
        return len(T_sims[T_sims > T_actual]) / nsims