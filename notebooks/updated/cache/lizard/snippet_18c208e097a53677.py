def _pd_post_process(self, cfg):
    loop_back_edges = self._cfg.get_loop_back_edges()
    for b1, b2 in loop_back_edges:
        successors = list(self._pd_graph_successors(cfg, b1))
        if len(successors) == 0:
            if b2 in self._post_dom:
                self._post_dom.add_edge(b1, b2)
            else:
                _l.debug('%s is not in post dominator dict.', b2)