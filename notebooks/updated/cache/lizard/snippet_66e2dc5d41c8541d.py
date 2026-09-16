def neighbors(self, key):
    return {n: attr['bond'] for n, attr in self.graph[key].items()}