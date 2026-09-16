def name2idfobject(idf, groupnamess=None, objkeys=None, **kwargs):
    if not objkeys:
        objkeys = idfobjectkeys(idf)
    for objkey in objkeys:
        idfobjs = idf.idfobjects[objkey.upper()]
        for idfobj in idfobjs:
            for key, val in kwargs.items():
                try:
                    if idfobj[key] == val:
                        return idfobj
                except BadEPFieldError as e:
                    continue