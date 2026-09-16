def Rx_matrix(theta):
    return np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.
        sin(theta), np.cos(theta)]])