def loadPng(varNumVol, tplPngSize, strPathPng):
    print('------Load PNGs')
    lstPngPaths = [None] * varNumVol
    for idx01 in range(0, varNumVol):
        lstPngPaths[idx01] = strPathPng + str(idx01) + '.png'
    aryPngData = np.zeros((tplPngSize[0], tplPngSize[1], varNumVol))
    for idx01 in range(0, varNumVol):
        aryPngData[:, :, (idx01)] = np.array(Image.open(lstPngPaths[idx01]))
    aryPngData = (aryPngData > 0).astype(int)
    return aryPngData