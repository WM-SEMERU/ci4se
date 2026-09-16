def needs_remesh(self):
    return (len(self.features) > 0 or self.is_misaligned or self.ecc != 0 or
        self.dynamics_method != 'keplerian')