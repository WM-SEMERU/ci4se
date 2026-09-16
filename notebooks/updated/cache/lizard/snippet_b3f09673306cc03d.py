def interpolation_points(self, N):
    if N == 1:
        return np.array([0.0])
    return np.cos(np.arange(N) * np.pi / (N - 1))