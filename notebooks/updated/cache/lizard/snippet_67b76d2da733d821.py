def extract_edges(self, feature_angle=30, boundary_edges=True,
    non_manifold_edges=True, feature_edges=True, manifold_edges=True,
    inplace=False):
    surf = self.extract_surface()
    return surf.extract_edges(feature_angle, boundary_edges,
        non_manifold_edges, feature_edges, manifold_edges, inplace=inplace)