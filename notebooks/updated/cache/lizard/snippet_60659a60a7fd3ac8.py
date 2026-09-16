def connect_near(self, source, target, weight):
    self.near_graph.add_edge(source, target, weight=weight, type='near')