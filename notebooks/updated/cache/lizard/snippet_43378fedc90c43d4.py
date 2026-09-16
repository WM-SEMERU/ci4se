def _run_on_node(self, node, state):
    l.debug('Analyzing block %#x, iteration %d.', node.addr, self.
        _node_iterations[node])
    concrete_state = state.get_concrete_state(node.addr)
    if concrete_state is None:
        l.error('_run_on_node(): cannot find any state for address %#x.',
            node.addr)
        return False, state
    state = state.copy()
    self._instates[node.addr] = state
    if self._node_iterations[node] >= self._max_iterations:
        l.debug('Skip node %s as we have iterated %d times on it.', node,
            self._node_iterations[node])
        return False, state
    state.register_callbacks([concrete_state])
    successors = self.project.factory.successors(concrete_state, addr=node.
        addr, size=node.size, opt_level=0)
    output_states = successors.all_successors
    state.concrete_states = [state for state in output_states if not state.
        ip.symbolic]
    self._outstates[node.addr] = state
    self._node_iterations[node] += 1
    return True, state