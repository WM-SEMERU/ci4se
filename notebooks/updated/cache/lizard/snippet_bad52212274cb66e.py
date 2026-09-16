def getBothEdges(self, label=None):
    if label:
        for edge in self.neoelement.relationships.all(types=[label]):
            yield Edge(edge)
    else:
        for edge in self.neoelement.relationships.all():
            yield Edge(edge)