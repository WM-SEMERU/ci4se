def applyMassCalMs1(msrunContainer, specfile, dataFit, **kwargs):
    toleranceMode = kwargs.get('toleranceMode', 'relative')
    if toleranceMode == 'relative':
        for si in msrunContainer.getItems(specfile, selector=lambda si: si.
            msLevel == 1):
            mzArr = msrunContainer.saic[specfile][si.id].arrays['mz']
            corrArr = dataFit.corrArray(mzArr)
            mzArr *= 1 + corrArr
    elif toleranceMode == 'absolute':
        for si in msrunContainer.getItems(specfile, selector=lambda si: si.
            msLevel == 1):
            mzArr = msrunContainer.saic[specfile][si.id].arrays['mz']
            corrArr = dataFit.corrArray(mzArr)
            mzArr += corrArr
    else:
        raise Exception('#TODO: a proper exception text')