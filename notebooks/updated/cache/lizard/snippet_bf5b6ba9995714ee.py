def valid_modes(self):
    default_mode = (self.mode,) if self.mode is not None else None
    return getattr(self, '_valid_mode', default_mode)