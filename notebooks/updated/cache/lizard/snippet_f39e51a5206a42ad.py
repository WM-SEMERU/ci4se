def get_func(fullFuncName):
    lastDot = fullFuncName.rfind('.')
    funcName = fullFuncName[lastDot + 1:]
    modPath = fullFuncName[:lastDot]
    aMod = get_mod(modPath)
    aFunc = getattr(aMod, funcName)
    assert callable(aFunc), '%s is not callable.' % fullFuncName
    return aFunc