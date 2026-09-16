def sow(self):
    for var_name in self.sow_vars:
        this_seed = getattr(self, var_name)
        for this_type in self.agents:
            setattr(this_type, var_name, this_seed)