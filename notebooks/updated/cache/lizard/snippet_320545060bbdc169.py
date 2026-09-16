def is_valid(self):
    if len(self.geometry) == 0:
        return True
    try:
        referenced = {self.graph[i][1] for i in self.graph.nodes_geometry}
    except BaseException:
        return False
    ok = referenced == set(self.geometry.keys())
    return ok