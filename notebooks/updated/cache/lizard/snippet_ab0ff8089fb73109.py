def loadNiiData(lstNiiFls, strPathNiiMask=None, strPathNiiFunc=None):
    print('---------Loading nii data')
    if strPathNiiMask is not None:
        aryMask = nb.load(strPathNiiMask).get_data().astype('bool')
    if strPathNiiFunc is not None:
        lstNiiFls = [os.path.join(strPathNiiFunc, i) for i in lstNiiFls]
    aryFunc = []
    for idx, path in enumerate(lstNiiFls):
        print('------------Loading run: ' + str(idx + 1))
        niiFunc = nb.load(path).get_data()
        if strPathNiiMask is not None:
            aryFunc.append(niiFunc[(aryMask), :])
        else:
            aryFunc.append(niiFunc)
    aryFunc = np.concatenate(aryFunc, axis=-1)
    aryFunc = aryFunc.astype('float32')
    return aryFunc