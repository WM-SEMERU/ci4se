def dependent(self, dep_type, node):
    self._dependents[dep_type] = self._dependents.get(dep_type, []) + [node]
    return self