def referenced_vertices(self):
    if len(self.entities) == 0:
        return np.array([], dtype=np.int64)
    referenced = np.concatenate([e.points for e in self.entities])
    referenced = np.unique(referenced.astype(np.int64))
    return referenced