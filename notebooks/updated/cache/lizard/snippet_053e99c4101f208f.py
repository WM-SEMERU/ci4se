def load_params_from_file(self, fname: str, allow_missing_params: bool=False):
    super().load_params_from_file(fname)
    self.module.set_params(arg_params=self.params, aux_params=self.
        aux_params, allow_missing=allow_missing_params)