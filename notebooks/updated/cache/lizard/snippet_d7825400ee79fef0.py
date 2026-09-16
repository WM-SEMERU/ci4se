def getsinIm(alat):
    alat = np.float64(alat)
    return 2 * np.sin(np.radians(alat)) / np.sqrt(4 - 3 * np.cos(np.radians
        (alat)) ** 2)