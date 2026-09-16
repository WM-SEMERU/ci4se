def has_predecessor(self, u, v):
    if u not in self.vertices:
        raise GraphInsertError("Vertex %s doesn't exist." % (u,))
    return u in self.pred and v in self.pred[u]