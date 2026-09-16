def sobel(image, mask=None):
    return np.sqrt(hsobel(image, mask) ** 2 + vsobel(image, mask) ** 2)