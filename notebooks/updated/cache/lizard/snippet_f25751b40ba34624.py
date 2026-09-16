def calc_state_matrix(self):
    system = self.system
    Gyx = matrix(system.dae.Gx)
    self.solver.linsolve(system.dae.Gy, Gyx)
    self.As = matrix(system.dae.Fx - system.dae.Fy * Gyx)
    return self.As