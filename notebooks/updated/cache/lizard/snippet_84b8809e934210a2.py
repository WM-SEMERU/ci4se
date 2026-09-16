def effectiv_num_data_points(self, kwargs_lens, kwargs_source,
    kwargs_lens_light, kwargs_ps):
    num_linear = 0
    if self._image_likelihood is True:
        num_linear = self.image_likelihood.num_param_linear(kwargs_lens,
            kwargs_source, kwargs_lens_light, kwargs_ps)
    num_param, _ = self.param.num_param()
    return self.num_data - num_param - num_linear