def operate_multi(self, points):
    points = np.array(points)
    affine_points = np.concatenate([points, np.ones(points.shape[:-1] + (1,
        ))], axis=-1)
    return np.inner(affine_points, self.affine_matrix)[(...), :-1]