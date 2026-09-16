def extractfields(data, commdct, objkey, fieldlists):
    objindex = data.dtls.index(objkey)
    objcomm = commdct[objindex]
    objfields = []
    for dct in objcomm[0:]:
        try:
            thefieldcomms = dct['field']
            objfields.append(thefieldcomms[0])
        except KeyError as err:
            objfields.append(None)
    fieldindexes = []
    for fieldlist in fieldlists:
        fieldindex = []
        for item in fieldlist:
            if isinstance(item, int):
                fieldindex.append(item)
            else:
                fieldindex.append(objfields.index(item) + 0)
        fieldindexes.append(fieldindex)
    theobjects = data.dt[objkey]
    fieldcontents = []
    for theobject, fieldindex in zip(theobjects, fieldindexes):
        innerlst = []
        for item in fieldindex:
            try:
                innerlst.append(theobject[item])
            except IndexError as err:
                break
        fieldcontents.append(innerlst)
    return fieldcontents