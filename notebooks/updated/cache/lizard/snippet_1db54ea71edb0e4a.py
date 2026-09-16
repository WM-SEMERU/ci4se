def alpha(self, x, y, kwargs, k=None):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    bool_list = self._bool_list(k)
    x_, y_, kwargs_copy = self._update_foreground(x, y, kwargs)
    f_x, f_y = np.zeros_like(x_), np.zeros_like(x_)
    for i, func in enumerate(self.func_list):
        if bool_list[i] is True:
            if self._model_list[i] == 'SHEAR':
                f_x_i, f_y_i = func.derivatives(x, y, **kwargs[i])
            else:
                f_x_i, f_y_i = func.derivatives(x_, y_, **kwargs_copy[i])
            f_x += f_x_i
            f_y += f_y_i
    return f_x, f_y