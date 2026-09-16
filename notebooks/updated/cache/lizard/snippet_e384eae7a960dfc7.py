def getFullParList(configObj):
    plist = []
    for par in configObj.keys():
        if isinstance(configObj[par], configobj.Section):
            plist.extend(getFullParList(configObj[par]))
        else:
            plist.append(par)
    return plist