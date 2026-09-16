def preprocess(img):
    img = img[35:195]
    img = img[::2, ::2, (0)]
    img[img == 144] = 0
    img[img == 109] = 0
    img[img != 0] = 1
    return img.astype(np.float).ravel()