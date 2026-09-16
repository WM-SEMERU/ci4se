def ReadTif(tifFile):
    img = Image.open(tifFile)
    img = np.array(img)
    return img