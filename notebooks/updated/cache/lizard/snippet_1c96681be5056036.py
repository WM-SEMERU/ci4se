def _post_process(self):
    loop_back_edges = self._cfg.get_loop_back_edges()
    for b1, b2 in loop_back_edges:
        self._graph.add_edge(b1, b2)