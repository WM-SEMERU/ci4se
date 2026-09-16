def extract_pixels(X):
    if len(X.shape) != 4:
        raise ValueError(
            'Array of input images has to be a 4-dimensional array of shape[n_images, n_pixels_y, n_pixels_x, n_bands]'
            )
    new_shape = X.shape[0] * X.shape[1] * X.shape[2], X.shape[3]
    pixels = X.reshape(new_shape)
    return pixels