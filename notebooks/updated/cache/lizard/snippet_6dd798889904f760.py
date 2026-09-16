def rgb2gray(img):
    T = np.linalg.inv(np.array([[1.0, 0.956, 0.621], [1.0, -0.272, -0.647],
        [1.0, -1.106, 1.703]]))
    r_c, g_c, b_c = T[0]
    r, g, b = np.rollaxis(as_float_image(img), axis=-1)
    return r_c * r + g_c * g + b_c * b