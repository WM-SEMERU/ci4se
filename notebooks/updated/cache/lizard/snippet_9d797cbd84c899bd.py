def make_bubble_surface(dims=DEFAULT_DIMS, repeat=3):
    gradients = make_gradients(dims)
    return np.sin((gradients[0] - 0.5) * repeat * np.pi) * np.sin((
        gradients[1] - 0.5) * repeat * np.pi)