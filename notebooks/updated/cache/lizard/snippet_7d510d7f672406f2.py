def is_complete(self):
    return all([(node.route_allocation() is not None) for node in list(self
        ._nodes.values()) if node != self._problem.depot()])