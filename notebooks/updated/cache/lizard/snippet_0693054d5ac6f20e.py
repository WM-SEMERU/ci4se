def _get_callsites(self, function_address):
    all_predecessors = []
    nodes = self.get_all_nodes(function_address)
    for n in nodes:
        predecessors = list(self.get_predecessors(n))
        all_predecessors.extend(predecessors)
    return all_predecessors