def _check_user_blacklists(self, f):
    return (not self._should_use_sim_procedures or f in self.
        _exclude_sim_procedures_list or f in self._ignore_functions or self
        ._exclude_sim_procedures_func is not None and self.
        _exclude_sim_procedures_func(f))