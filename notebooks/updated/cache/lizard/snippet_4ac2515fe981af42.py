def area_pipe_min(self):
    return (self.safety_factor * self.q / self.vel_critical).to(u.cm ** 2)