def _max(self, memory, addr, **kwargs):
    return memory.state.solver.max(addr, exact=kwargs.pop('exact', self.
        _exact), **kwargs)