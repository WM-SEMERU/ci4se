def measure_states(states, measurement_matrix, measurement_covariance):
    measurement_matrix = np.atleast_2d(measurement_matrix)
    measurement_covariance = np.atleast_2d(measurement_covariance)
    measurement_dim = measurement_matrix.shape[0]
    if measurement_covariance.shape != (measurement_dim, measurement_dim):
        raise ValueError(
            'Measurement matrix and covariance have inconsistent shapes {} and {}'
            .format(measurement_matrix.shape, measurement_covariance.shape))
    states = np.atleast_2d(states)
    if states.shape[0] == 0:
        return np.zeros((0, measurement_dim))
    measurement_means = measurement_matrix.dot(states.T).T
    measurement_noises = np.random.multivariate_normal(mean=np.zeros(
        measurement_dim), cov=measurement_covariance, size=states.shape[0])
    return measurement_means + measurement_noises