def select_by_ids(selname, idlist, selection_exists=False, chunksize=20,
    restrict=None):
    idlist = list(set(idlist))
    if not selection_exists:
        cmd.select(selname, 'None')
    idchunks = [idlist[i:i + chunksize] for i in range(0, len(idlist),
        chunksize)]
    for idchunk in idchunks:
        cmd.select(selname, '%s or (id %s)' % (selname, '+'.join(map(str,
            idchunk))))
    if restrict is not None:
        cmd.select(selname, '%s and %s' % (selname, restrict))