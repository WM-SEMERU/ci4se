def getreferingobjs(referedobj, iddgroups=None, fields=None):
    referringobjs = []
    idf = referedobj.theidf
    referedidd = referedobj.getfieldidd('Name')
    try:
        references = referedidd['reference']
    except KeyError as e:
        return referringobjs
    idfobjs = idf.idfobjects.values()
    idfobjs = list(itertools.chain.from_iterable(idfobjs))
    if iddgroups:
        idfobjs = [anobj for anobj in idfobjs if anobj.getfieldidd('key')[
            'group'] in iddgroups]
    for anobj in idfobjs:
        if not fields:
            thefields = anobj.objls
        else:
            thefields = fields
        for field in thefields:
            try:
                itsidd = anobj.getfieldidd(field)
            except ValueError as e:
                continue
            if 'object-list' in itsidd:
                refname = itsidd['object-list'][0]
                if refname in references:
                    if referedobj.isequal('Name', anobj[field]):
                        referringobjs.append(anobj)
    return referringobjs