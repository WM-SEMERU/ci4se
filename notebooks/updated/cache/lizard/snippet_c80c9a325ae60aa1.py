def face_adjacency_tree(self):
    segment_bounds = np.column_stack((self.vertices[self.
        face_adjacency_edges].min(axis=1), self.vertices[self.
        face_adjacency_edges].max(axis=1)))
    tree = util.bounds_tree(segment_bounds)
    return tree