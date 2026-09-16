def _conc_alloc_size(self, sim_size):
    if self.state.solver.symbolic(sim_size):
        size = self.state.solver.max_int(sim_size)
        if size > self.state.libc.max_variable_size:
            l.warning(
                'Allocation request of %d bytes exceeded maximum of %d bytes; allocating %d bytes'
                , size, self.state.libc.max_variable_size, size)
            size = self.state.libc.max_variable_size
    else:
        size = self.state.solver.eval(sim_size)
    return size