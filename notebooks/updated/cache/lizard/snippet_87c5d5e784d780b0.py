def add_background(image, sigma_bkd):
    if sigma_bkd < 0:
        raise ValueError(
            'Sigma background is smaller than zero! Please use positive values.'
            )
    nx, ny = np.shape(image)
    background = np.random.randn(nx, ny) * sigma_bkd
    return background