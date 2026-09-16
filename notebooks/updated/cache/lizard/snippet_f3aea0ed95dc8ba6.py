def _q_iteration(self, Q, Bpp_solver, Vm, Va, pq):
    dVm = -Bpp_solver.solve(Q)
    Vm[pq] = Vm[pq] + dVm
    V = Vm * exp(1.0j * Va)
    return V, Vm, Va