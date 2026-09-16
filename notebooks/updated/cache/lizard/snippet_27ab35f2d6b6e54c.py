def createMask(input=None, static_sig=4.0, group=None, editpars=False,
    configObj=None, **inputDict):
    if input is not None:
        inputDict['static_sig'] = static_sig
        inputDict['group'] = group
        inputDict['updatewcs'] = False
        inputDict['input'] = input
    else:
        print >> sys.stderr, 'Please supply an input image\n'
        raise ValueError
    configObj = util.getDefaultConfigObj(__taskname__, configObj, inputDict,
        loadOnly=not editpars)
    if configObj is None:
        return
    if not editpars:
        run(configObj)