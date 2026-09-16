def get_range(self, process_err_pct=0.05):
    vel = self.vel + 5 * randn()
    alt = self.alt + 10 * randn()
    self.pos += vel * self.dt
    err = self.pos * process_err_pct * randn()
    slant_range = (self.pos ** 2 + alt ** 2) ** 0.5 + err
    return slant_range