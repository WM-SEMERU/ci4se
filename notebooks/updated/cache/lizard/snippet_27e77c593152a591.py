def remove(self, predicate=None, obj=None):
    self.graph.remove((self.asNode(), predicate, obj))