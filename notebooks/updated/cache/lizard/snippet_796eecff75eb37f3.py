def get_options_dict(self):
    d = self.synchronizer.options if self.synchronizer else {}
    d.update(self.extra_opts)
    return d