def _find_input_dependencies(self, inputs):
    dependencies = []
    for address in inputs:
        dependencies.extend(self._predecessor_tree.find_read_predecessors(
            address))
    return dependencies