def crtPwBoxCarFn(varNumVol, aryPngData, aryPresOrd, vecMtDrctn):
    print('------Create pixel-wise boxcar functions')
    aryBoxCar = np.empty(aryPngData.shape[0:2] + (len(vecMtDrctn),) + (
        varNumVol,), dtype='int64')
    for ind, num in enumerate(vecMtDrctn):
        aryCondTemp = np.zeros(aryPngData.shape, dtype='int64')
        lgcTempMtDrctn = [aryPresOrd == num][0]
        aryCondTemp[:, :, (lgcTempMtDrctn)] = np.copy(aryPngData[:, :, (
            lgcTempMtDrctn)])
        aryBoxCar[:, :, (ind), :] = aryCondTemp
    return aryBoxCar