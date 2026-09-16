def _get_kriging_matrix(self, n):
    if self.coordinates_type == 'euclidean':
        xy = np.concatenate((self.X_ADJUSTED[:, (np.newaxis)], self.
            Y_ADJUSTED[:, (np.newaxis)]), axis=1)
        d = cdist(xy, xy, 'euclidean')
    elif self.coordinates_type == 'geographic':
        d = core.great_circle_distance(self.X_ADJUSTED[:, (np.newaxis)],
            self.Y_ADJUSTED[:, (np.newaxis)], self.X_ADJUSTED, self.Y_ADJUSTED)
    a = np.zeros((n + 1, n + 1))
    a[:n, :n] = -self.variogram_function(self.variogram_model_parameters, d)
    np.fill_diagonal(a, 0.0)
    a[(n), :] = 1.0
    a[:, (n)] = 1.0
    a[n, n] = 0.0
    return a