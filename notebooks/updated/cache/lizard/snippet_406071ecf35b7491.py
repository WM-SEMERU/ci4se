def findScopedPar(theDict, scope, name):
    if len(scope):
        theDict = theDict[scope]
    return theDict, theDict[name]