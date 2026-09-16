def photaddline(tab, sourceid):
    colnames = tab[0].keys()
    tmpdict = dict()
    for i in range(len(tab)):
        if tab[i]['source_id'] != sourceid:
            continue
        for elem in colnames:
            if elem not in ['comments', 'epoch', 'instrument_id',
                'magnitude', 'magnitude_unc', 'publication_id', 'system',
                'telescope_id']:
                tmpdict[elem] = tab[i][elem]
            elif elem == 'band':
                continue
            else:
                tmpstr = tab[i]['band'] + '.' + elem
                tmpdict[tmpstr] = tab[i][elem]
    return tmpdict