def init_graph(self):
    self._graph = Graph()
    for key in self.loader.disk_fixtures.keys():
        self.graph.add_node(key)
    for key, fixture in self.loader.disk_fixtures.items():
        for dependency in fixture.dependencies:
            self.graph.add_dependency(key, dependency)