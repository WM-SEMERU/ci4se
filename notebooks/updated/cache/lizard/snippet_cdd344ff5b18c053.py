def median(input=None, configObj=None, editpars=False, **inputDict):
    if input is not None:
        inputDict['input'] = input
    else:
        raise ValueError('Please supply an input image')
    configObj = util.getDefaultConfigObj(__taskname__, configObj, inputDict,
        loadOnly=not editpars)
    if configObj is None:
        return
    if not editpars:
        run(configObj)