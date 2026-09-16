def concretize_read_addr(self, addr, strategies=None):
    if isinstance(addr, int):
        return [addr]
    elif not self.state.solver.symbolic(addr):
        return [self.state.solver.eval(addr)]
    strategies = self.read_strategies if strategies is None else strategies
    return self._apply_concretization_strategies(addr, strategies, 'load')