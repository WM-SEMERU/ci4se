def do(self):
    if not self._nodes:
        return
    node_copy = dict(self._nodes)
    self._do(node_copy)
    return self._factory.get_instantiated_services()