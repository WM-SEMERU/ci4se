def register_func(self, func_name, func_kwargs):
    self.scan_funcs.append(func_name)
    self.scan_kwargs.append(func_kwargs)