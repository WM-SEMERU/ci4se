def step_state(self, state, successor_func=None, **run_args):
    try:
        successors = self.successors(state, successor_func=successor_func,
            **run_args)
        stashes = {None: successors.flat_successors, 'unsat': successors.
            unsat_successors, 'unconstrained': successors.
            unconstrained_successors}
    except (SimUnsatError, claripy.UnsatError) as e:
        if self._hierarchy:
            self._hierarchy.unreachable_state(state)
            self._hierarchy.simplify()
        stashes = {'pruned': [state]}
    except tuple(self._resilience) as e:
        self._errored.append(ErrorRecord(state, e, sys.exc_info()[2]))
        stashes = {}
    return stashes