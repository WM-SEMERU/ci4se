def _raw(cls, vertices, edges, out_edges, in_edges, head, tail):
    self = object.__new__(cls)
    self._out_edges = out_edges
    self._in_edges = in_edges
    self._head = head
    self._tail = tail
    self._vertices = vertices
    self._edges = edges
    return self