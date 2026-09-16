def open(self):
    if self._state != 'open':
        if self._line is not None:
            self._state = 'open'
            self._nodes = self.grid.graph.nodes_from_line(self._line)
            self.grid.graph.remove_edge(self._nodes[0], self._nodes[1])
        else:
            raise ValueError('``line`` is not set')