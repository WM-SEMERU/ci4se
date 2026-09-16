def _analyze(self):
    self._pre_analysis()
    if self._graph_visitor is None:
        self._analysis_core_baremetal()
    else:
        self._analysis_core_graph()
    self._post_analysis()