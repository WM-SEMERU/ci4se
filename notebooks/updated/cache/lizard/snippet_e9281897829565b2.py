def _construct_control_flow_slice(self, simruns):
    if self._cfg is None:
        l.error('Please build CFG first.')
    cfg = self._cfg.graph
    for simrun in simruns:
        if simrun not in cfg:
            l.error('SimRun instance %s is not in the CFG.', simrun)
    stack = []
    for simrun in simruns:
        stack.append(simrun)
    self.runs_in_slice = networkx.DiGraph()
    self.cfg_nodes_in_slice = networkx.DiGraph()
    self.chosen_statements = {}
    while stack:
        block = stack.pop()
        if block.addr not in self.chosen_statements:
            self.chosen_statements[block.addr] = True
            predecessors = cfg.predecessors(block)
            for pred in predecessors:
                stack.append(pred)
                self.cfg_nodes_in_slice.add_edge(pred, block)
                self.runs_in_slice.add_edge(pred.addr, block.addr)