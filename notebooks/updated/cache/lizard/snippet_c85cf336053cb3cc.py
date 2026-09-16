def mass_2d(self, r, kwargs, bool_list=None):
    bool_list = self._bool_list(bool_list)
    mass_2d = 0
    for i, func in enumerate(self.func_list):
        if bool_list[i] is True:
            kwargs_i = {k: v for k, v in kwargs[i].items() if not k in [
                'center_x', 'center_y']}
            mass_2d_i = func.mass_2d_lens(r, **kwargs_i)
            mass_2d += mass_2d_i
    return mass_2d