def pushpopitem(self, key, value, node_factory=_Node):
    heap = self._heap
    position = self._position
    precedes = self._precedes
    prio = self._keyfn(value) if self._keyfn else value
    node = node_factory(key, value, prio)
    if key in self:
        raise KeyError('%s is already in the queue' % repr(key))
    if heap and precedes(heap[0].prio, node.prio):
        node, heap[0] = heap[0], node
        position[key] = 0
        del position[node.key]
        self._sink(0)
    return node.key, node.value