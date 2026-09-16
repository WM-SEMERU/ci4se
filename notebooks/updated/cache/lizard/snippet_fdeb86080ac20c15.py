def H_n(self, n, x):
    n_array = np.zeros(n + 1)
    n_array[n] = 1
    return hermite.hermval(x, n_array, tensor=False)