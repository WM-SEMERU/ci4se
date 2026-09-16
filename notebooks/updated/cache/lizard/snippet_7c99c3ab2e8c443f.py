def check_solver(self, kwargs_lens, kwargs_ps, kwargs_cosmo={}):
    if self._solver is True:
        image_x, image_y = kwargs_ps[0]['ra_image'], kwargs_ps[0]['dec_image']
        image_x, image_y = self.real_image_positions(image_x, image_y,
            kwargs_cosmo)
        dist = self._solver_module.check_solver(image_x, image_y, kwargs_lens)
        return np.max(dist)
    else:
        return 0