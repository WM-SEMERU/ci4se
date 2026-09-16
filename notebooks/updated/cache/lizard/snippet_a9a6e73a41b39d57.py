def hull(self):
    from scipy.spatial import ConvexHull
    if len(self.coordinates) >= 4:
        inds = ConvexHull(self.coordinates).vertices
        return self.coordinates[inds]
    else:
        return self.coordinates