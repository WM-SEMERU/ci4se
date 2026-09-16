def diffFromDefaults(theTask, report=False):
    defaultTree = load(theTask, canExecute=False, strict=True, defaults=True)
    thisTree = load(theTask, canExecute=False, strict=True, defaults=False)
    defaultFlat = cfgpars.flattenDictTree(defaultTree)
    thisFlat = cfgpars.flattenDictTree(thisTree)
    diffFlat = dict(set(thisFlat.items()) - set(defaultFlat.items()))
    if report:
        defaults_of_diffs_only = {}
        for k in diffFlat:
            defaults_of_diffs_only[k] = defaultFlat[k]
        msg = 'Non-default values of "' + str(theTask) + '":\n' + _flat2str(
            diffFlat) + """

Default values:
""" + _flat2str(
            defaults_of_diffs_only)
        print(msg)
    return diffFlat